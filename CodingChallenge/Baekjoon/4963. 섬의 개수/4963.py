LAND = '1'
SEA = '0'
dx = [-1, 0, 1, -1, 1, -1, 0, 1]
dy = [-1, -1, -1, 0, 0, 1, 1, 1]

def count_land(field):
    count = 0
    next = []
    visit = set()
    for y in range(len(field)):
        for x in range(len(field[0])):
            # 탐색할 곳이 없다면 가보지 않은 섬을 찾는다.
            if (y, x) in visit or field[y][x] == SEA:
                continue
            count += 1
            next.append((y, x))
            visit.add((y, x))

            # 탐색을 진행한다.
            for now in next:
                now_y, now_x = now
                # 상하좌우 대각선들에 대해 연결 확인
                for i in range(8):
                    next_y, next_x = (now_y + dy[i]), (now_x + dx[i])
                    if 0 <= next_y < len(field) and 0 <= next_x < len(field[0]) and (next_y, next_x) not in visit and field[next_y][next_x] != SEA:
                        next.append((next_y, next_x))
                        # print(now, "=>", (next_y, next_x), field[next_y][next_x])
                        visit.add((next_y, next_x))  # 해당칸 방문처리
    return count


while True:
    w, h = map(int, input().split())
    if (w, h) == (0, 0):
        break
    field = [[] for i in range(h)]
    for i in range(h):
        field[i].extend(input().split())

    # 섬갯수 확인 진행
    result = count_land(field)

    # 결과 출력
    print(result)
