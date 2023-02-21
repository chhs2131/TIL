d = [99999] * 5001
d[0] = 0
for i in range(3, 5001):
    if d[i - 3] != 99999:
        d[i] = min(d[i], d[i - 3] + 1)
    if d[i - 5] != 99999:
        d[i] = min(d[i], d[i - 5] + 1)

result = d[int(input())]
if result != 99999:
    print(result)
else:
    print(-1)
