input()
nums = list(map(int, input().split()))
result = 0

for start in range(len(nums)):
    count = 1
    before_2nd = nums[start]
    before = nums[start]

    for now in range(len(nums)):
        if before < nums[now]:  # 증가하는지 확인
            before_2nd = before
            before = nums[now]
            count += 1
        elif before_2nd < nums[now] < before:  # 이전 수가 너무 컸던 것은 아닌지 확인
            before = nums[now]

    result = max(result, count)

print(result)
