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
