n = int(input()) + 1

d = [0] * n
d[0] = 1
d[1] = 3
for i in range(2, n):
    d[i] = (d[i - 1] * 2 + d[i - 2]) % 9901

print(d[n - 1])
