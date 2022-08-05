import heapq

# 입력
n, d = map(int, input().split())
shortcut = [[] for _ in range(10001)]  # shortcut[시작위치] -> [0:도착위치][1:비용]
all_node = [0, d]

# 입력받은 지름길을 그래프 형태로 제작
for _ in range(n):
    s, e, dist = map(int, input().split())
    if e <= d and s <= d:  # 목적지를 지나쳐가는 것은 패스
        shortcut[s].append([e, dist])
        all_node.append(s)
        all_node.append(e)

# 지름길 없이 가는 경로도 그래프에 추가
all_node = list(set(all_node))
all_node.sort()
for i in range(len(all_node) - 1):
    shortcut[all_node[i]].append([all_node[i + 1], all_node[i + 1] - all_node[i]])

# print("노드종류", all_node)
# print("이용가능한것", shortcut)

# 탐색
v = [False for _ in range(10001)]  # 방문여부
p = [99999 for _ in range(10001)]  # 비용
p[0] = 0
next_node = [0]
while next_node:
    # 방문 처리
    now_node = heapq.heappop(next_node)
    if now_node == d:  # 목적지 도착했는지 확인
        break
    elif v[now_node]:  # 이미 방문한 곳인지 확인
        continue
    v[now_node] = True
    # print("방문!!", now_node, " 기준가:", p[now_node], "=================")

    # 연결된 노드 확인
    for connected_node in shortcut[now_node]:
        end, price = connected_node
        # print("  정보", now_node, " => ", end, price)
        if not v[end]:  # 아직 방문하지 않은 곳이여야함
            p[end] = min(p[end], p[now_node] + price)  # 비용 산정 (현재까지의 비용 + 가야할곳의 비용)
            # print("    가격정정", end, " => ", p[end], p[now_node] + price)
        heapq.heappush(next_node, end)

# 목적지까지의 비용 출력
print(p[d])
