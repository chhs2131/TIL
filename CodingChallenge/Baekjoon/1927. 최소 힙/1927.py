import sys
import heapq

pq = []
n = int(input())
for i in range(0, n):
    number = int(sys.stdin.readline())  # input으로 받으면 느림
    if number == 0:
        if not pq:
            print(0)
        else:
            print(heapq.heappop(pq))
    else:
        heapq.heappush(pq, int(number))
