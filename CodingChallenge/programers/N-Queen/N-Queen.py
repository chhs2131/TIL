count = 0


def can_pos(board, now):
    for i in range(now):
        if board[i] == board[now] or abs(board[now] - board[i]) == now - i:
            return False
    return True


def dfs(now_line, brd, n):
    global count
    if now_line == n:  # Queen을 모두 사용한경우 카운트
        count += 1
        return

    for i in range(n):  # 해당 줄에 모든 칸을 살펴본다.
        brd[now_line] = i
        if can_pos(brd, now_line):
            dfs(now_line + 1, brd, n)


def solution(n):
    board = [-1 for i in range(n)]
    dfs(0, board, n)
    return count
