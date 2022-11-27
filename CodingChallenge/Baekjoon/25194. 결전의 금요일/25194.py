from collections import defaultdict

a = input()
while True:
    n = list(map(int, input().split()))

    int_dict = defaultdict(bool)
    weekday = [True, False, False, False, False, False, False]
    can = False
    now = 0  # 7로 나눈 나머지가 현재 요일이다. 0월1화2수3목4금, 금요일은 +4
    for time in n:
        t = time % 7

        print(int_dict)
        add_list = []
        for i in range(0, 7):
            if not weekday[i]:  # 월화수목금토일 중 시작지점인 요일에 대해서만 진행
                continue

            need = -(i + t - 4) % 7  # 금요일까지 몇 일이 필요한지 계산  0 + 3 - 4
            if need < 0:
                need += 7

            print("[현재숫자:", t, "요일:", i, "] 필요숫자:", need, int_dict[need])
            if need == 0 or int_dict[need]:  # 가능한지 확인
                can = True
                break
            else:
                add_list.append((i + t) % 7)

        if can:
            break
        for w in add_list:
            weekday[w] = True  # 불가능한경우 현재 요일도 시작지점으로 추가.
        int_dict[t] = True  # 실패한 숫자는 다른 요일과 덧셈할 수 있도록 추가

    if can:
        print("YES")
    else:
        print("NO")
