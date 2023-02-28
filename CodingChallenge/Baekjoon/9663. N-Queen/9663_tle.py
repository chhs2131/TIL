import copy

dx = [-1, 0, 1]


def make_board(depth, i, new_board):
    board_size = len(new_board)
    new_board[depth][i] = True
    for j in range(board_size - depth):
        for move_x in dx:
            now_y = depth + j
            now_x = i + move_x * j
            if now_y < board_size and 0 <= now_x < board_size:
                new_board[now_y][now_x] = True
    return new_board


# 입력 및 변수 초기화
n = int(input())
board = [[False] * n for _ in range(n)]

# 경우의 수 탐색
count = 0
next_step = [(0, board)]  # depth, board
while next_step:
    # 상태 하나를 가져오고, 배치가 완료되었으면 경우의수 +1
    depth, now_board = next_step.pop()

    # 해당라인에 모든칸에 대해 배치가능한지 확인
    for i in range(n):
        if not now_board[depth][i]:
            if depth + 1 == n:  # 완성된 경우 경우의 수 추가
                count += 1
            else:
                new_board = make_board(depth, i, copy.deepcopy(now_board))
                next_step.append((depth + 1, new_board))

# 출력
print(count)
