import itertools

n, m = map(int, input().split())
nums = range(1, n + 1)
result = list(itertools.combinations(nums, m))
print(result)

# for r in result:
#     print(*r)  # 가변인자로 전달
