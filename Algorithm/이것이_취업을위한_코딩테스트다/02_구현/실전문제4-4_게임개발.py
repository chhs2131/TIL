# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
LAND = 0
NOT_VISIT = 0
SEA = 1
VISITED = 1


n, m = map(int, input().split())

d = [[0] * m for _ in range(n)]
x, y, direction = map(int, input().split())
d[x][y] = 1  # 현재 좌표 방문 처리

# 전체 맵 정보 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))




def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


# 시뮬레이션
count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if d[nx][ny] == NOT_VISIT and array[nx][ny] == LAND:  # 정면에 가보지 않은 칸이 잇을 때
        d[nx][ny] = VISITED
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    # 4방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if array[nx][ny] == SEA:
            # 뒤가 바다로 막혀있다면 탐색을 종료한다.
            break

        x = nx
        y = ny
        turn_time = 0

print(count)
