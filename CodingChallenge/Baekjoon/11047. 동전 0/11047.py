n, k = map(int, input().split())
coin = []
for i in range(0, n):
    c = int(input())
    if c <= k: (coin.append(c))

amount = 0
coin.reverse()
for i in coin:
    a = int(k / i)
    k -= i * a
    amount += a
    # print("step : ", i, k, amount)
    if k == 0:
        break

print(amount)
