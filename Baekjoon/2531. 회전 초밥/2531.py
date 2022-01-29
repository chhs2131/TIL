import sys

n, d, k, c = map(int, input().split())  # n접시의수, d초밥의 가짓수, k연속으로먹어야되는접시수, c쿠폰번호
dish = []
for i in range(0, n):
    dish.append(int(sys.stdin.readline()))

point = 0
count = 0
while point < n:
    # 확인할 범위 가져오기
    over = (point + k) - n
    if over <= 0:  # 확인할 범위가 리스트 범위내인 경우
        now_eat = dish[point:point+k]
    else:
        now_eat = dish[point:n] + dish[0:over]

    # 중복되지않은 가지수 확인
    now_count = len(set(now_eat))
    try:
        aaa = now_eat.index(c)
    except:
        now_count += 1  # 쿠폰 적용하기

    # 최고값 갱신
    if count < now_count:
        count = now_count

    # print("범위: "+str(point)+"~"+str(point+k), "범위초과:", over, "현재값:", now_count, "항목:", now_eat)
    point += 1  # 한칸증진
print(count)
