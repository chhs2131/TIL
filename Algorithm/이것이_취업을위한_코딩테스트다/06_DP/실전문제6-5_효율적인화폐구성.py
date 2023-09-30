
n, m = map(int, input().split())
coin = []
for i in range(n):
    coin.append(int(input()))

d = [99999] * 10001
d[0] = 0
for i in range(m + 1):
    for c in coin:
        d[i] = min(d[i], d[i - c] + 1)

if d[m] == 99999:
    print(-1)
else:
    print(d[m])
