def bfs(p, rg):
    row = len(p)
    column = len(p[0])
    v = [[False] * column for _ in range(0, row)]
    q = []
    count = 0
    for i in range(0, row):
        for j in range(0, column):
            if not v[i][j]:  # 모든칸에 대해 방문을 진행한다.
                q.append([i, j])
                v[i][j] = True
                count += 1
            while q:
                r, c = q.pop(0)  # 큐에서 하나를 꺼내 어떤 색인지 확인
                color = p[r][c]

                for k in range(0, 4):
                    next_row = r + my[k]
                    next_column = c + mx[k]
                    if (0 <= next_column < column) and (0 <= next_row < row):  # 가능범위안에 있고 아직 방문하지 않았다면
                        if not v[next_row][next_column]:
                            next_color = p[next_row][next_column]
                            if (next_color == color) or (rg and color != 'B' and next_color != 'B'):
                                # 다음색상을 확인해 동일하면 큐에 추가 (조건문: 좌측 일반인, 우측 적록색약)
                                q.append([next_row, next_column])
                                v[next_row][next_column] = True
    return count


mx = [1, -1, 0, 0]
my = [0, 0, 1, -1]
n = int(input())
picture = []
for i in range(0, n):
    picture.append(list(input()))

print(bfs(picture, False), bfs(picture, True))
