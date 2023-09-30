n = int(input())
d = [[0] * (n + 1) for _ in range(10)]
for i in range(10):
    d[i][1] = 1

result = 1  # 0도 오르막 수
for i in range(1, 10):
    for j in range(1, n + 1):
        d[i][j] = d[i - 1][j] + d[i][j - 1]
        result = (result + d[i][j]) % 10007

print(result)
