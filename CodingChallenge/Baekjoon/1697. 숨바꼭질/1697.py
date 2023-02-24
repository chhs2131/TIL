import collections

me, target = map(int, input().split())
visit = [False] * 100001


def isValied(pos):
    global visit
    if 0 <= pos <= 100000 and not visit[pos]:
        return True
    return False


def search():
    global visit, me, target

    result = 987654321
    next = collections.deque()
    next.append((me, 0))  # pos, sec
    visit[me] = True
    i = 0
    while next:
        pos, sec = next.popleft()
        if pos == target:
            result = min(result, sec)

        if isValied(pos * 2):
            visit[pos * 2] = True
            next.append((pos * 2, sec + 1))

        if isValied(pos - 1):
            visit[pos - 1] = True
            next.append((pos - 1, sec + 1))

        if isValied(pos + 1):
            visit[pos + 1] = True
            next.append((pos + 1, sec + 1))

    return result


if target <= me:
    print(me - target)
else:
    print(search())
