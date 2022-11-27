from collections import defaultdict
number = defaultdict(bool)

# 보유하고 있는 정수 입력받기
input()
data = input().split()
for num in data:
    number[num] = True

# 찾고싶은 정수 입력받기
input()
data = input().split()
for num in data:
    if number[num]:
        print("1")
    else:
        print("0")
