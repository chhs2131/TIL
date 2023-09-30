import itertools

n, m = map(int, input().split())
nums = list(range(1, n + 1))
result = list(itertools.product(nums, repeat=m))
for r in result:
    print(*r)
