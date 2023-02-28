def is_good_board(depth, t_board):
    board_size = len(t_board)
    for j in range(depth):
        # print("  ", t_board[j], t_board[depth], depth - j, abs(t_board[depth] - t_board[j]))
        if t_board[j] == t_board[depth] or depth - j == abs(t_board[depth] - t_board[j]):
            return False
    return True

n = int(input())
count = 0
board = [0] * n
next_one = [(-1, board)]  # depth, board
while next_one:
    depth, now_board = next_one.pop()

    for i in range(n):
        new_board = now_board.copy()
        new_board = now_board
        new_board[depth + 1] = i
        if is_good_board(depth + 1, new_board):
            if depth + 1 == n - 1:
                count += 1
            else:
                next_one.append((depth + 1, new_board))

print(count)
