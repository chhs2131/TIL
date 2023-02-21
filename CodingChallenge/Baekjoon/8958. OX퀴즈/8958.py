n = int(input())
for i in range(n):
    answer = input().split('X')
    result = 0
    for a in answer:
        result += (len(a) + 1) * len(a) / 2
    print(int(result))
