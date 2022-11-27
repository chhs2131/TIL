T = int(input())
for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    if a < 10 and b < 10:
        result = a * b
    else:
        result = -1
    print("#"+str(test_case), result)
