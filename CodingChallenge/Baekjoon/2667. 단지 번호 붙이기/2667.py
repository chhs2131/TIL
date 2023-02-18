NEW_HOUSE = '1'
EMPTY = '0'
dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]


n = int(input())
tile = []
for i in range(n):
    tile.append(list(input()))

count = -1
result = []
for y in range(n):
    for x in range(n):
        if tile[y][x] != NEW_HOUSE:
            continue

        count += 1
        result.append(0)
        next_tile = [(y, x)]
        while next_tile:
            now_y, now_x = next_tile.pop()
            # print(now_y, now_x, "=>", tile[now_y][now_x], next_tile)
            if tile[now_y][now_x] == NEW_HOUSE:
                tile[now_y][now_x] = count
                result[count] += 1

            for i in range(4):
                next_y = now_y + dy[i]
                next_x = now_x + dx[i]
                # print("  ", next_y, next_x)
                if (0 <= next_y < n) and (0 <= next_x < n) and (tile[next_y][next_x] == NEW_HOUSE):
                    tile[next_y][next_x] = count
                    result[count] += 1
                    next_tile.append((next_y, next_x))

print(len(result))
result.sort()
for r in result:
    print(r)
