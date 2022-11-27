import heapq
import sys
from collections import defaultdict
input = sys.stdin.readline

case = int(input())
for c in range(case):
    max_h = []
    min_h = []
    v = defaultdict(int)

    k = int(input())
    for i in range(k):
        command, number = input().split()
        number = int(number)
        if command == 'I':  # 우선순위큐에 값 추가
            heapq.heappush(min_h, number)
            heapq.heappush(max_h, -number)
            v[number] += 1
        else:
            if number == 1:  # 우선순위큐에서 최대/최소값 제거
                while max_h:
                    num = -heapq.heappop(max_h)
                    if v[num] != 0:  # 0인 경우 이미 방문한 곳이다.
                        v[num] -= 1
                        break
            else:
                while min_h:
                    num = heapq.heappop(min_h)
                    if v[num] != 0:
                        v[num] -= 1
                        break

    # 출력 (최대/최소순, 비어있는경우 EMPTY)
    while max_h and v[-max_h[0]] == 0:  # 힙에 방문한곳이 남아있다면 제외해준다.
        heapq.heappop(max_h)
    while min_h and v[min_h[0]] == 0:
        heapq.heappop(min_h)
    if max_h:
        print(-max_h[0], min_h[0])
    else:
        print("EMPTY")
