import sys
input = sys.stdin.readline
GOOD = 1
VISITED = 2

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

n = int(input())
for i in range(n):
    width, height, amount = map(int, input().split())

    farm = [[0 for __ in range(width)] for _ in range(height)]
    for j in range(amount):
        x, y = map(int, input().split())
        farm[y][x] = GOOD

    count = 0
    for y in range(height):
        for x in range(width):
            next = []
            if farm[y][x] == GOOD:
                next.append((y, x))
                farm[y][x] = VISITED
                count += 1

            while next:
                now_y, now_x = next.pop()
                for l in range(4):
                    next_y = now_y + dy[l]
                    next_x = now_x + dx[l]
                    if (0 <= next_y < height) and (0 <= next_x < width) and (farm[next_y][next_x] == GOOD):
                        next.append((next_y, next_x))
                        farm[next_y][next_x] = VISITED

    print(count)
