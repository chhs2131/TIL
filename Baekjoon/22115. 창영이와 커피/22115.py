# 입력
n, k = map(int, input().split())
c = list(map(int, input().split()))

# 변수 초기화
can = [100001 for _ in range(k + 1)]
can[0] = 0

# 적은 커피로 많은 카페인을!
for coffee in c:
    can_temp = can.copy()
    for num in range(coffee, k + 1):
        can_temp[num] = min(can[num], can[num - coffee] + 1)
    can = can_temp.copy()

# 출력
if can[k] == 100001:
    print(-1)
else:
    print(can[k])
