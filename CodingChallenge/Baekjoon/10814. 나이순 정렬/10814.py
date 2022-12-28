class Person:
    def __init__(self, index, age, name):
        self.index = index
        self.name = name
        self.age = age

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def get_index(self):
        return self.index


# 입력
people = []
n = int(input())
for i in range(n):
    age, name = input().split(' ')
    people.append(Person(i, int(age), name))

# 정렬
people = sorted(people, key=lambda person: (person.get_age(), person.get_index()))

# 출력
for person in people:
    print(person.get_age(), person.get_name())
