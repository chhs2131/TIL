#
# 효율성 테스트 실패 (시간초과) - Astar 휴리스틱 문제?
#
import heapq


def near_wasd(maps, visited, x_max, y_max, x, y):
    near = []

    # 상 [-1][0]
    if y - 1 >= 0 and maps[y - 1][x] == 1 and not visited[y - 1][x]:
        near.append((y - 1, x))
    # 하 [+1][0]
    if y + 1 < y_max and maps[y + 1][x] == 1 and not visited[y + 1][x]:
        near.append((y + 1, x))
    # 좌 [0][-1]
    if x - 1 >= 0 and maps[y][x - 1] == 1 and not visited[y][x - 1]:
        near.append((y, x - 1))
    # 우 [0][+1]
    if x + 1 < x_max and maps[y][x + 1] == 1 and not visited[y][x + 1]:
        near.append((y, x + 1))

    return near


def solution(maps):
    answer = -1
    x_max = len(maps[0])
    y_max = len(maps)

    # 변수 생성
    v = [[False for _ in range(x_max)] for _ in range(y_max)]
    v[0][0] = True
    n = [(0, 1, 0, 0)]  # 평가함수, 현재까지실제비용, y좌표, x좌표

    # 탐색 진행
    while n:
        _, count, y, x = heapq.heappop(n)

        # 상하좌우 열린공간 확인
        for yt, xt in near_wasd(maps, v, x_max, y_max, x, y):
            heapq.heappush(n, (count + 1 + (y_max - 1 - yt) + (x_max - 1 - xt), count + 1, yt, xt))

            # 목적지에 도착한 경우 프로그램 종료
            if xt == x_max - 1 and yt == y_max - 1:
                answer = count + 1
                break

            # 현재 위치 방문 처리
            v[y][x] = True

    # 결과 리턴
    return answer
