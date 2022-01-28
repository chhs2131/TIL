if __name__ == "__main__":
    n, m = map(int, input().split())
    maze = []
    for i in range(0, n):
        maze.append(list(input()))

    q = [[0, 0]]  # 다음 방문할 칸
    c = [[0]*m for _ in range(n)]  # 비용
    c[0][0] = 1
    while q:
        # 큐에서 하나를 꺼낸다.
        ny, nx = q.pop(0)
        # print("=> x", nx, ", y", ny, c[ny][nx])

        # 목적지인지 확인한다. 맞으면 탐색을 끝낸다.
        if ny == m-1 and nx == n-1:
            break

        # 현재칸 주변에 아직 방문해보지 못한 칸을 큐에 추가한다.
        for j in range(4):
            if j == 0 and nx - 1 > -1:  # 좌
                if maze[ny][nx-1] != '0':
                    if c[ny][nx - 1] == 0:
                        c[ny][nx - 1] = c[ny][nx] + 1
                        q.append([ny, nx - 1])
                        # print("r", maze[ny][nx-1])
            elif j == 1 and nx + 1 < m:  # 우
                if maze[ny][nx+1] != '0':
                    if c[ny][nx + 1] == 0:
                        c[ny][nx + 1] = c[ny][nx] + 1
                        q.append([ny, nx + 1])
                        # print("r", maze[ny][nx+1])
            elif j == 2 and ny - 1 > -1:  # 상
                if maze[ny-1][nx] != '0':
                    if c[ny - 1][nx] == 0:
                        c[ny - 1][nx] = c[ny][nx] + 1
                        q.append([ny - 1, nx])
                        # print("u", maze[ny-1][nx])
            elif j == 3 and ny + 1 < n:  # 하
                if maze[ny+1][nx] != '0':
                    if c[ny + 1][nx] == 0:
                        c[ny + 1][nx] = c[ny][nx] + 1
                        q.append([ny + 1, nx])
                        # print("d", maze[ny+1][nx])

    # 최종 비용을 출력한다.
    print(c[n-1][m-1])
