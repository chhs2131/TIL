n = int(input())

result = -1
if n // 10 == 0:
    result = n

count = 9
i = 9
while True:
    if i > 9876543210:
        break
    # print(i)
    # 탐색
    flag = False
    number = str(i)
    for j in range(len(number) - 1):
        # 감소하는 수 규칙에 위반되는 경우
        if number[j] <= number[j + 1]:
            new_number = number[0:j] + str(int(number[j]) + 1) + '0' * (len(number) - j - 1)  # 9에 대해서도 처리필요
            # print("  => change to", new_number,
            #       "first", number[0:j],
            #       "plus", str(int(number[j]) + 1),
            #       "zero", '0' * (len(number) - j - 1))
            i = int(new_number)
            flag = True
            break
        # 감소하는 수인 경우
        elif j == len(number) - 2:
            count += 1

    # i가 새로 설정된 경우 다시 시작
    if flag:
        continue

    # print(count, ": ", i)
    # n번째 값을 찾았을 경우
    if count == n:
        result = i
        break
    i += 1

print(result)
