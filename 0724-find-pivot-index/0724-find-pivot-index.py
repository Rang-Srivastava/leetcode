class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n=len(nums)
        left=0
        total=sum(nums)
        for i in range(0,n):
            right=total-nums[i]-left
            if left==right:
                return i 
            left+=nums[i]
        return -1
        
        