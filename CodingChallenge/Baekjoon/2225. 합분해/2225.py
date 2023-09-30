MM = 201

d = [[1] * MM for _ in range(MM)]
for k in range(1, MM):
    for target in range(1, MM):
        d[k][target] = (d[k - 1][target] + d[k][target - 1]) % 1000000000

n, k = map(int, input().split())
print(d[k - 1][n])
