import sys
input = sys.stdin.readline

n = int(input())
before = list(map(int, input().split()))

now = [-1, -1, -1]
for i in range(n - 1):
    now = list(map(int, input().split()))
    now[0] = min(now[0] + before[1], now[0] + before[2])
    now[1] = min(now[1] + before[0], now[1] + before[2])
    now[2] = min(now[2] + before[0], now[2] + before[1])
    before = now

print(min(now))
