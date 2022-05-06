import random
SIZE = 5
POPULATION_SIZE = 4
MUTATION_RATE = 0.05
MAX_GENERATION = 1000


#######################################################################################################################
#
# define class, function
#
#######################################################################################################################
class Chromosome:  # 염색체
    def __init__(self, g=[]):
        self.genes = g.copy()  # 유전자는 리스트로 구현된다.
        self.fitness = 0  # 적합도
        if self.genes.__len__() == 0:  # 염색체가 초기 상태이면 초기화 된다.
            i = 0
            while i < SIZE:
                if random.random() >= 0.5:
                    self.genes.append(1)
                else:
                    self.genes.append(0)
                i += 1

    def cal_fitness(self):  # 적합도를 계산한다.
        self.fitness = 0
        value = 0
        for i in range(SIZE):
            value += self.genes[i] * pow(2, SIZE - 1 - i)
        self.fitness = value
        return self.fitness

    def __str__(self):
        return self.genes.__str__()


def print_p(pop):
    i = 0
    for x in pop:
        print("염색체 #", i, "=", x, "적합도=", x.cal_fitness())
        i += 1
    print("")


def select(pop):  # 선택 연산
    max_value = sum([c.cal_fitness() for c in population])
    pick = random.uniform(0, max_value)
    current = 0

    # 룰렛휠에서 어떤 조각에 속하는지를 알아내는 루프
    for c in pop:
        current += c.cal_fitness()
        if current > pick:
            return c


def crossover(pop):  # 교차 연산
    father = select(pop)
    mother = select(pop)
    print(" - 부모유전자 ")
    print("    -", father)
    print("    -", mother)
    index = random.randint(1, SIZE - 2)
    child1 = father.genes[:index] + mother.genes[index:]
    child2 = mother.genes[:index] + mother.genes[index:]
    return (child1, child2)


def mutate(c):  # 돌연변이 연산
    for i in range(SIZE):
        if random.random() < MUTATION_RATE:
            if random.random() < 0.5:
                c.genes[i] = 1
            else:
                c.genes[i] = 0


#######################################################################################################################
#
# main
#
#######################################################################################################################
population = []
i = 0

# 초기 염색체를 생성하여 객체 집단에 추가한다.
while i < POPULATION_SIZE:
    population.append(Chromosome())
    i += 1

count = 0
population.sort(key=lambda x: x.cal_fitness(), reverse=True)
print("세대 번호=", count)
print_p(population)
count = 1

while population[0].cal_fitness() < 31:
    new_pop = []

    # 선택과 교차 연산
    for _ in range(int(POPULATION_SIZE / 2)):
        c1, c2 = crossover(population)
        new_pop.append(Chromosome(c1))
        new_pop.append(Chromosome(c2))

    # 자식세대가 부모세대를 대체한다. (깊은복사)
    population = new_pop.copy()

    # 돌연변이 연산
    for c in population:
        mutate(c)

    # 출력을 위한 정렬
    population.sort(key=lambda x: x.cal_fitness(), reverse=True)
    print("세대 번호=", count)
    print_p(population)
    count += 1
    if count > MAX_GENERATION:
        break
