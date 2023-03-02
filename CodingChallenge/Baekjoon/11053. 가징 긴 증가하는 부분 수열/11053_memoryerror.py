import itertools

input()
numbers = list(map(int, input().split()))
now_result = 0
max_result = 0

for i in range(1, len(numbers) + 1):
    nums = list(itertools.combinations(numbers, i))

    # print("=============", i)

    for num in nums:
        before = 0
        count = 0
        # print("             ", num)
        for j in range(len(num)):
            if before < num[j]:
                count += 1
                before = num[j]
        now_result = max(now_result, count)

    # print(max_result, now_result)
    if max_result < now_result:
        max_result = now_result
    else:
        break

print(max_result)
