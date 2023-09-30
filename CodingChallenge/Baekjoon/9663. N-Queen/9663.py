n = int(input())
count = 0
board = [0] * n


def is_good_board(depth):
    for j in range(depth):
        # print("  ", t_board[j], t_board[depth], depth - j, abs(t_board[depth] - t_board[j]))
        if board[j] == board[depth] or depth - j == abs(board[depth] - board[j]):
            return False
    return True


def dfs(depth):
    global count
    for i in range(n):
        board[depth] = i
        if is_good_board(depth):
            if depth == n - 1:
                count += 1
            else:
                dfs(depth + 1)


dfs(0)
print(count)
