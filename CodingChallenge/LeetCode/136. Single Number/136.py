class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = {}
        for num in nums:
            if num in result:
                result[num] = False
            else:
                result[num] = True

        print(result)
        fin = 0
        for r in result:
            if result[r] == True:
                fin = r
                break

        return fin
