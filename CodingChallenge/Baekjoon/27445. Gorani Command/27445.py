h, w = map(int, input().split())
if h == 1 and w == 1:
    input()
    print(1, 1)
else:
    # 제일 짧은 좌표와 비용을 기억한다.
    shortest_pos = (1, 1)
    shortest_dis = 999999

    for i in range(0, h - 1):
        now_dis = int(input())
        if now_dis < shortest_dis:
            shortest_dis = now_dis
            shortest_pos = (i + 1, 1)

    x = list(map(int, input().split()))
    for i in range(len(x)):
        now_dis = x[i]
        if now_dis < shortest_dis:
            shortest_dis = now_dis
            shortest_pos = (h, i + 1)

    # 그게 y 좌표면 x칸 만큼 더하면 되고, 그게 x 좌표면 y칸 만큼 빼면 된다.
    y, x = shortest_pos
    if x == 1:
        print(y, x + shortest_dis)
    elif y == h:
        print(y - shortest_dis, x)
