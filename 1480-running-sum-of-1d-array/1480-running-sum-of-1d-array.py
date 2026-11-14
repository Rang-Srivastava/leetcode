class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        total = 0

        for i in range(n):
            total = total + nums[i]
            result.append(total)

        return result