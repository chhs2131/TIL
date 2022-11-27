import re
n = int(input())  # 입력받기
word = []
for i in range(0, n):
    word.append(input())

number = []
for i in range(0, n):  # 각 줄에서 숫자값만 반환
    regex = re.findall("[0-9]*", word[i])
    number.extend(regex)
number = ' '.join(number).split()  # 전체값을 정렬
number = list(map(int, number))
number.sort()

for i in number:  # 정답출력
    print(i)
