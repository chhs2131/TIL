# f(n) = g(n) + h(n)
# g(n) = 시작노드로부터의 거리
# h(n) = 제 위치에 있지 않은 타일 개수

from queue import PriorityQueue
from random import randint

marked2 = []

class State:
    goal: str = ''

    def __init__(self, board: str, moves: int = 0):
        self.board = board
        self.moves = moves

    def __lt__(self, other):
        # 비교 연산자 < 오버로딩. 우선순위큐를 사용하기 위해 필요함
        return self.f() < other.f()

    def f(self):  # 상태함수
        return self.g() + self.h()

    def g(self):  # 지금까지 경로 비용
        return self.moves

    def h(self):  # 휴리스틱
        dist = 0
        size = 3
        for n in range(9):
            piece = self.goal[n]
            goal_x = n // size
            goal_y = n - goal_x * size
            board_x = self.board.index(piece) // size
            board_y = self.board.index(piece) - board_x * size
            dist += abs(goal_x - board_x) + abs(goal_y - board_y)
        return dist


def bfs(start: State, goal: str) -> dict:
    que = PriorityQueue()
    que.put(start)
    marked = {start.board: None}
    while que and (current := que.get()).board != goal:
        for state in expand(current):
            if state.board not in marked:
                marked[state.board] = current.board
                marked2.append(state)
                que.put(state)
    return marked


def exchange(state: State, prev_pos: int, new_pos: int) -> State:
    new_board = list(state.board)
    new_board[prev_pos], new_board[new_pos] = new_board[new_pos], new_board[prev_pos]
    return State(''.join(new_board), state.moves + 1)


def expand(state: State) -> list:
    result = []
    position = state.board.index('0')
    if position not in (0, 1, 2):  # UP
        result.append(exchange(state, position, position - 3))
    if position not in (0, 3, 6):  # LEFT
        result.append(exchange(state, position, position - 1))
    if position not in (2, 5, 8):  # RIGHT
        result.append(exchange(state, position, position + 1))
    if position not in (6, 7, 8):  # DOWN
        result.append(exchange(state, position, position + 3))
    return result


def pprint(board: str):
    print(' '.join(board[:3]))
    print(' '.join(board[3:6]))
    print(' '.join(board[6:]))
    print('-----')

def print_path(start: str, goal: str, marked):
    path = []
    node = goal
    while node != start:
        path.append(node)
        node = marked[node]
    path.append(start)
    for each in path[::-1]:
        pprint(each)


def main():
    global marked2
    start = State('283164705')
    State.goal = '123804765'
    marked = bfs(start, State.goal)
    print("====[ 해 답 ]====")
    print_path(start.board, State.goal, marked)
    # print(len(marked))

    print("\n====[ 전 체 ]====")
    for sss in marked2:
        print(str(sss.f())+" = "+str(sss.g())+"+"+str(sss.h()))
        pprint(sss.board)


if __name__ == '__main__':
    main()
