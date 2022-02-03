def z_search(n, r, c):
    if r == 0 and c == 0:
        return 0
    elif r == 0 and c == 1:
        return 1
    elif r == 1 and c == 0:
        return 2
    elif r == 1 and c == 1:
        return 3
    result = 4 * z_search(n-1, int(r/2), int(c/2))  # return값 * 4
    result = result + 2*(r % 2) + (c % 2)  # 나누면서 버림된 숫자를 더 해줌
    return result


board_size, row, column = map(int, (input().split()))
print(z_search(board_size, row, column))


'''
# 한칸씩 스탭을 세려고 했던 코드 (작성하다가 말았다.)
def z_search(board_size):
    global step, r, c
    print(board_size, step)
    # return
    if board_size == 1:
        for i in range(0, 4):
            step += 1
            if r == r and c == c:  # 찾는 좌표가 맞는 경우
                return step
    # 진행문
    else:
        for i in range(0, 4):  # 좌상, 우상, 좌하, 우하
            z_search(board_size - 1)


n, r, c = map(int, (input().split()))
step = -1
z_search(n)
print(step)
'''