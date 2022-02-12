import sys
input = sys.stdin.readline


def index_check(index_number):
    global n
    if index_number >= (n * 2):
        gap = index_number - (n * 2)
        index_number = 0 + abs(gap)
    elif index_number < 0:
        index_number = (n * 2) - 1
    return index_number


def robot_is_there(belt_number):
    global q
    robot_index = -1
    try:
        robot_index = q.index(belt_number)
    except:
        pass
    return robot_index


n, k = map(int, input().split())
# belt = list(map(int, input().split()))
belt = list(map(int, input().split()))
q = []  # belt_number

starting_point = 0
end_point = 0
broken_tile = 0
step = 0
count = 1
while broken_tile < k:  # 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.
    step += 1
    if step > 3:
        step = 1
        count += 1
    # print(step, "] ["+str(starting_point)+":"+ str(end_point)+"]", belt, q)

    if step == 1:  # 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
        starting_point -= 1
        starting_point = index_check(starting_point)
    elif step == 2:  # 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
        ra = len(q)
        for i in range(ra):
            r = q.pop(0)
            ti = index_check(r + 1)
            ri = robot_is_there(ti)
            if (ri == -1) and (belt[ti] != 0):  # 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
                q.append(ti)
                belt[ti] -= 1
            else:
                q.append(r)
    elif step == 3:  # 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
        if belt[starting_point] != 0:
            q.append(starting_point)
            belt[starting_point] -= 1

    end_point = index_check(starting_point + n - 1)   # 내릴 수 있는 로봇이 있는지 확인.
    ri = robot_is_there(end_point)
    if ri != -1:
        d = q.pop(ri)
    broken_tile = belt.count(0)  # 내구도가 0인곳 갯수 확인

print(count)
