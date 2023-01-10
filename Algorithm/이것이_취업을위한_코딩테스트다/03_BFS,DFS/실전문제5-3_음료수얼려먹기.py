n, m = map(int, input().split())

# 2차원 list 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))


# DFS
def dfs(x, y):
    # 범위 내인지 확인
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 아직 방문하지 않은 노드라면
    if graph[x][y] == 0:
        # 방문처리
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


# 모든 노드에 대해 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)
