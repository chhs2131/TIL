import itertools

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

result = list(itertools.combinations_with_replacement(nums, m))
for r in result:
    print(*r)
