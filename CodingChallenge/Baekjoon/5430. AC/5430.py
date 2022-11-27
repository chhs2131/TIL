import re

t = int(input())
for i in range(0, t):
    command = list(input())
    left = int(input())
    number_list = input()
    nl = re.findall(r'\d+', number_list)

    reverse = False
    error = False
    start = 0
    end = len(nl)
    for c in command:
        if c == 'R':  # R(뒤집기)
            reverse = not reverse
        else:  # D(버리기)
            if left == 0:  # 배열내에 원소가 없는데 버리려고 하는경우
                error = True
                break
            else:
                if reverse:
                    end -= 1
                else:
                    start += 1
                left -= 1

    # 결과출력
    nl = nl[start:end]
    if not error:
        if reverse:
            nl.reverse()
        result = '[' + str(','.join(nl)) + ']'
        print(result)
    else:
        print("error")
