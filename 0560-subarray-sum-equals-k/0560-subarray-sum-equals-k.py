class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        prefix_map={0:1}
        current_sum=0
        count=0
        for i in range(0,n):
            current_sum+=nums[i]
            if current_sum-k in prefix_map:
                count+=prefix_map[current_sum-k]
            prefix_map[current_sum]=prefix_map.get(current_sum,0)+1
        return count

        