# 입력 item(무게,가치)
n, k = map(int, input().split())
item = []
for _ in range(n):
    item.append(list(map(int, input().split())))

# 각 물건별 가방 리스트
p = [[0 for _ in range(k + 1)] for _ in range(n)]

# 계산 (각 물건을 넣을 공간을 마련하고 물건을 넣었을 때 가치 확인)
for i in range(n):
    now_item_weight, now_item_value = item[i]
    for j in range(1, k + 1):
        if j < now_item_weight:
            p[i][j] = p[i - 1][j]
        else:
            p[i][j] = max(p[i - 1][j], p[i - 1][j - now_item_weight] + now_item_value)

# 출력
print(p.pop().pop())
