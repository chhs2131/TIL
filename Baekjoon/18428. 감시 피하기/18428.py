from itertools import combinations
'''
def cardinal_point(aaa):
    if aaa == 0:
        return '동'
    if aaa == 1:
        return '서'
    if aaa == 2:
        return '남'
    if aaa == 3:
        return '북'
'''

def seek(teacher):
    global p
    for t in teacher:
        ty, tx = t
        for i in range(0, 4):  # 동서남북 확인
            now_x = tx
            now_y = ty
            # print("[" + cardinal_point(i) + "] ", "y:", now_y, "x:", now_x)
            while True:
                now_y += ewsn[i][0]
                now_x += ewsn[i][1]
                if (0 <= now_x < n) and (0 <= now_y < n):  # 복도 범위 내를 탐색하고 있는지 확인
                    now_tile = p[now_y][now_x]
                    # print(" ", now_tile, now_y, now_x)
                    if now_tile == 'S':
                        return False
                    elif now_tile == 'O':
                        break
                    elif now_tile == 'T':
                        break
                else:
                    break
    return True


# 입력받기, n(보드크기), p(보드배치.. s=학생, t=선생, x=빈칸) - 선생님의 수는 5이하, 학생의 수는 30이하의, 빈 칸의 개수는 3개 이상.
n = int(input())
p = []
teacher = []
empty = []
ewsn = [[0, 1], [0, -1], [1, 0], [-1, 0]]
for i in range(0, n):
    p.append(list(input().split()))

for i in range(0, n):  # 선생님,빈칸의 좌표 기억
    for j in range(0, n):
        if p[i][j] == 'X':
            empty.append([i, j])
        elif p[i][j] == 'T':
            teacher.append([i, j])

# 로직실행
can = False
for xy in list(combinations(empty, 3)):
    for y, x in xy:
        p[y][x] = 'O'
    if seek(teacher):
        can = True
        break
    for y, x in xy:
        p[y][x] = 'X'

if can:
    print("YES")
else:
    print("NO")
