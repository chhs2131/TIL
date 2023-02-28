import itertools
n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

result = list(itertools.product(nums, repeat=m))
for r in result:
    print(*r)
