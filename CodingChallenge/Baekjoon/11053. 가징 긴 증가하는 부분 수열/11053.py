input()
nums = list(map(int, input().split()))

dp = [1] * 1001
for i in range(1, len(nums)):
    # print("======[" + str(i) + " : "  + str(nums[i]) + "]=====")
    for j in range(1, i + 1):
        # print(nums[i] <= nums[i - j], nums[i - j])
        if nums[i] <= nums[i - j]:
            continue
        else:
            dp[i] = max(dp[i], dp[i - j] + 1)
    # print(dp)

print(max(dp))
