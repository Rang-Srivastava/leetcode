class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        right=0
        sum=0
        n=len(nums)
        res=float('inf')
        while right < n:
            sum = sum + nums[right]
            while sum >= target:
                length = right - left + 1
                res = min (res,length)
                sum = sum-nums[left]
                left+=1
            right+=1
        return 0 if res == float('inf') else res
        
        