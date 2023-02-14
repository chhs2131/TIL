d = [0] * 99999
d[1] = 1
d[2] = 1
for i in range(3, 10001):
    d[i] = d[i - 1] + d[i - 2]

n = int(input())
for i in range(n):
    target, div = map(int, input().split())
    print("Case #" + str(i + 1) + ":", d[target] % div)
