import sys
import heapq

n = int(input())
q = []
for i in range(0, n):
    temp = int(sys.stdin.readline())
    if temp == 0:
        try:
            print(-heapq.heappop(q))
        except:
            print(0)
    else:
        heapq.heappush(q, -temp)
