x = int(input())

d = [0] * 30001  # 필요한 연산 횟수가 기록됨
for i in range(2, x + 1):
    # 1을 빼는 경우
    d[i] = d[i - 1] + 1
    # 2로 나눠지는 경우
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    # 3로 나눠지는 경우
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    # 5로 나눠지는 경우
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)
print(d[x])
