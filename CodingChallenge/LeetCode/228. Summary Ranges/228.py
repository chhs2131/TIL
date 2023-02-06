class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []

        index = 0
        while index < len(nums):
            start = nums[index]
            end_index = self.findNextNumber(nums, index)
            self.addResult(result, start, nums[end_index])
            index = end_index + 1
        return result

    def findNextNumber(self, nums, index):
        start = nums[index]
        now = start
        while index < len(nums) - 1:
            nextNumber = nums[index + 1]
            if now + 1 != nextNumber:
                break
            now = nextNumber
            index += 1
        return index

    def addResult(self, result, start, end):
        if start == end:
            result.append(str(start))
        else:
            result.append(str(start) + "->" + str(end))
