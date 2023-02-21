s, m = map(int, input().split())

# 집합 S 입력받기
dic = {}
for i in range(s):
    dic[input()] = True

# M 개의 문자열에 대해 확인
count = 0
for i in range(m):
    string = input()
    if dic.get(string) is True:
        count += 1
print(count)
