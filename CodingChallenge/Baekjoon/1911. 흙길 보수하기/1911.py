# 입력받기  n물웅덩이수, l널빤지길이, pos물웅덩이위치
n, l = map(int, input().split())
pos = []
for i in range(0, n):
    pos.append(list(map(int, input().split())))

# 물웅덩이 정렬
pos.sort()

# 로직 실행
amount = 0
last = 0
for i in range(0, n):
    # 웅덩이 시작start ~ 끝end 지점 파악
    start = pos[i][0]
    if start <= last:
        start = last
    end = pos[i][1]
    if end - 1 < last:
        continue

    # 수량추가 및 보수공사끝난지점 갱신
    amount += int((end-start)/l)
    if (end-start) % l != 0:
        amount += 1
        last = start + l * (int((end-start)/l) + 1)
    else:
        last = end

# 출력
print(amount)
