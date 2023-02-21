import sys
input = sys.stdin.readline
n = int(input())

num = []
for i in range(n):
    cost, reward = map(int, input().split())
    num.append((cost, reward))
num.reverse()

d = [0] * 20
for i in range(n):
    cost, reward = num[i]

    d[i] = d[i - 1]
    if i - cost + 1 < 0:
        continue
    d[i] = max(d[i], reward + d[i - cost])

print(d[n - 1])
