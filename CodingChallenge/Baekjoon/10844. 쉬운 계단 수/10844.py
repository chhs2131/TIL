l = int(input())
if l == 1:
    print(9)
else:
    d = [[0] * 10 for _ in range(101)]
    for i in range(1, 10):
        d[1][i] = 1

    for i in range(2, 101):
        for j in range(10):
            if j == 0:
                d[i][0] = d[i - 1][1]
            elif j == 9:
                d[i][9] = d[i - 1][8]
            else:
                d[i][j] = d[i - 1][j - 1] + d[i - 1][j + 1]

    result = 0
    for n in d[l]:
       result += n
    print(result % 1000000000)
