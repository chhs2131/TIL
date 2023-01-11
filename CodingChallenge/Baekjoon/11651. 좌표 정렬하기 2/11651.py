import sys
input = sys.stdin.readline

n = int(input())

array = []
for i in range(n):
    x, y = map(int, input().split())
    array.append((x, y))

array.sort(key=lambda pos: (pos[1], pos[0]))  # 정렬 우선 순위: y축 1순위, x축 2순위
for a in array:
    print(a[0], a[1])
