def normal_type(aaa):
    aaa %= 8
    if aaa < 0:
        aaa += 8  # 음수일 경우 8을 더한다.
    return aaa


t = []
for i in range(4):
    t.append(list(input()))  # N극0, S극1

focus = [0, 0, 0, 0]
k = int(input())
for i in range(k):  # 회전시킬 톱니바퀴 번호, 방향(1시계, -1반시계)
    number, turn = input().split()
    odd = False
    if int(number) % 2 == 1:
        odd = True

    moved = [False, False, False, False]  # 움직였는지
    q = [int(number)]
    while q:
        x = q.pop(-1)
        if not moved[x - 1]:  # 아직 안움직인 톱니바퀴 일 때, 움직인다.
            # 연결되있는 놈을 큐에 추가. [0][2] = [1][6], [1][2] = [2][6], [2][2] = [3][6] 서로 다른극일때 움직임
            if x-1 == 0 or x-1 == 1 or x == 1:
                if t[0][normal_type(focus[0] + 2)] != t[1][normal_type(focus[1] + 6)]:
                    q.append(1)
                    q.append(2)
            if x-1 == 1 or x-1 == 2 or x == 2:
                if t[1][normal_type(focus[1] + 2)] != t[2][normal_type(focus[2] + 6)]:
                    q.append(2)
                    q.append(3)
            if x-1 == 2 or x-1 == 3 or x == 3:
                if t[2][normal_type(focus[2] + 2)] != t[3][normal_type(focus[3] + 6)]:
                    q.append(3)
                    q.append(4)
            if x == 4:
                if t[2][normal_type(focus[2] + 2)] != t[3][normal_type(focus[3] + 6)]:
                    q.append(3)

            if odd and x % 2 == 1:  # 톱니바퀴를 돌린다.
                focus[int(x) - 1] -= int(turn)
            elif not odd and x % 2 == 0:
                focus[int(x) - 1] -= int(turn)
            else:
                focus[int(x) - 1] += int(turn)
            moved[x - 1] = True

score = 0  # 점수 부여
for i in range(4):  # 각 톱니바퀴의 12시방향에 S가 있는지 확인한다
    nf = normal_type(focus[i])
    if i == 0 and t[0][nf] == '1':  score += 1
    if i == 1 and t[1][nf] == '1':  score += 2
    if i == 2 and t[2][nf] == '1':  score += 4
    if i == 3 and t[3][nf] == '1':  score += 8
print(score)
