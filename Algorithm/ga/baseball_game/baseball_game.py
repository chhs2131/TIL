import random
POPULATION_SIZE = 5
MUTATION_RATE = 0.1
MAX_GENERATION = 100000


class Chromosome:  # 염색체
    size = 0
    genes = []
    fitness = 0
    strike = 0
    ball = 0

    def __init__(self, n, g=[]):
        self.size = n
        self.genes = g.copy()
        self.fitness = 0

        if self.genes.__len__() == 0:  # 초기 상태일 경우 초기화 진행
            for i in range(n):
                do_while = True
                while do_while or number in self.genes:
                    do_while = False
                    number = str(int(random.random() * 10))
                self.genes.append(number)

    def cal_fitness(self, target):  # 적합도 확인
        value = 0
        s = 0
        b = 0
        for i in range(self.size):
            if self.genes[i] == target[i]:
                value += self.size / 2 + 1
                s += 1
            elif self.genes[i] in target:
                value += 1
                b += 1
        self.strike = s
        self.ball = b
        self.fitness = value
        return self.fitness

    def __str__(self):
        return self.genes.__str__()

    def get_strike(self):
        return self.strike

    def get_ball(self):
        return self.ball


def print_p(pop, target):
    i = 0
    for x in pop:
        print("#", i, "=", x, "적합도=", x.cal_fitness(target), "(SB:", x.get_strike(),"/", x.get_ball(), ")")
        i += 1
    print("")


# 선택 연산
def select(pop, target):
    max_value = sum(c.cal_fitness(target) for c in pop)
    pick = random.uniform(0, max_value)
    current = 0

    for c in pop:  # 룰렛휠 선택
        current += c.cal_fitness(target)
        if current > pick:
            return c


# 교차연산 (부모 선택 후 -> 자식 탄생)
def crossover(n, pop, target):
    father = select(pop, target)
    mother = select(pop, target)
    index = random.randint(1, n - 2)
    child1 = father.genes[:index] + mother.genes[index:]
    child2 = mother.genes[:index] + father.genes[index:]
    return (child1, child2)


# 돌연변이
def mutate(size, pop):
    for i in range(size):
        if random.random() < MUTATION_RATE:
            do_while = True
            while do_while or number in pop.genes:
                do_while = False
                number = str(int(random.random() * 10))
            pop.genes[i] = number



#######################################################################################################################
#
# main
#
#######################################################################################################################
# 임의의 n자리 숫자를 입력한다. (숫자 중복 x)
target = list(input())
n = int(len(target))

# 목표 적합도 연산
target_score = (n / 2 + 1) * n
print("목표 적합도=", target_score, "\n")

# 클래스 초기화
population = []
for i in range(POPULATION_SIZE):
    population.append(Chromosome(n))
    # print(population[i].cal_fitness(target), "\n====================\n")

# GA 연산 시작
count = 0
population.sort(key=lambda x: x.cal_fitness(target), reverse=True)
print("세대 번호=", count)
print_p(population, target)
count = 1

while population[0].cal_fitness(target) < target_score:
    new_pop = []
    for _ in range(int(POPULATION_SIZE / 2)):  # 선택과 교차 연산
        c1, c2 = crossover(n, population, target)
        new_pop.append(Chromosome(n, c1))
        new_pop.append(Chromosome(n, c2))

    population = new_pop.copy()  # 세대교체

    for c in population:  # 돌연변이 연산
        mutate(n, c)

    population.sort(key=lambda x: x.cal_fitness(target), reverse=True)
    print("세대 번호=", count)
    print_p(population, target)
    count += 1
    if count > MAX_GENERATION:
        break  # 너무오래걸릴경우 탈출
