import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
for i in range(n):
    coins.append(int(input()))

d = [0] * 10001
d[0] = 1
for coin in range(n):
    for i in range(k + 1):
        value = coins[coin]
        if i - value < 0:
            continue
        d[i] += d[i - value]

print(d[k])
