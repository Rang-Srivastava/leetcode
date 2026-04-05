class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n=len(nums)
        curr_max=nums[0]
        max_sum=nums[0]
        curr_min=nums[0]
        min_sum=nums[0]
        total_sum=nums[0]
        for i in range(1,n):
            curr_max=max(curr_max+nums[i],nums[i])
            max_sum=max(max_sum,curr_max)
            curr_min=min(curr_min+nums[i],nums[i])
            min_sum=min(min_sum,curr_min)
            total_sum+=nums[i]
        if max_sum<0:
            return max_sum
        return max(max_sum,total_sum-min_sum)



        