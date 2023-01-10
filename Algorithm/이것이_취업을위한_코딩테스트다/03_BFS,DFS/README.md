# BFS/DFS

### 간선 표현 방식
인접 행렬 방식
- 모든 관계를 저장하므로 노드 개수가 많을수록 메모리 낭비 발생
- 특정 노드간에 관계를 O(1)로 확인할 수 있다.
```python
INF = 999999999

graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]
print(graph)
```
인접 리스트 방식
- 연결된 정보만을 저장하므로 메모리를 효율적으로 사용
- 하지만 특정 노드들이 연결되어있는지 확인하는 속도가 느림 (전체 탐색 필요)
```python
graph = [[] for _ in range(3)]

graph[0].append((1, 7))
graph[0].append((2, 5))
graph[1].append((0, 7))
graph[2].append((0, 5))
```

## 예제
### DFS
```python
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9
dfs(graph, 1, visited)
```

### BFS
```python
from collections import deque


def bfs(graph, start, visited):
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐에 내용이 있다면 계속 탐색 진행
    while queue:
        # 큐에서 하나에 원소를 뽑아낸다.
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된 노드들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9
bfs(graph, 1, visited)
```

### 예제 5-3 (음료수 얼려 먹기)
```python
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

```


### 실전문제 5-4 (미로탈출)
```python
from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위를 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문할때만 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단거리 반환
    return graph[n - 1][m - 1]


print(bfs(0, 0))
```