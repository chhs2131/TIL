import heapq
import sys


def pop_min_abs(neg_list, pos_list):
    result = 0
    if neg_list and pos_list:
        if neg_list[0] <= pos_list[0]:
            result = -(heapq.heappop(neg_list))
        else:
            result = heapq.heappop(pos_list)
    elif neg_list:
        result = -(heapq.heappop(neg_list))
    elif pos_list:
        result = heapq.heappop(pos_list)
    return result


n = int(sys.stdin.readline())
maxh = []
minh = []
for i in range(n):
    x = int(sys.stdin.readline())
    if x < 0:  # 음수일경우
        heapq.heappush(minh, -x)
    elif x > 0:  # 양수일경우
        heapq.heappush(maxh, x)
    else:  # 0일경우
        print(pop_min_abs(minh, maxh))
