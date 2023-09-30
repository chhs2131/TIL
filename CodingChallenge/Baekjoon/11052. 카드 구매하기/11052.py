n = int(input())
cards = list(map(int, input().split()))

d = [0] * (n + 1)
for i in range(n + 1):
    for c in range(n):
        if i - c - 1 >= 0:
            d[i] = max(d[i], d[i - c - 1] + cards[c])

print(d[len(d) - 1])
