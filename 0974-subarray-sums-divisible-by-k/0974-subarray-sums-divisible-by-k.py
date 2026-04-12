class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n=len(nums)
        total_sum=0
        result=0
        remainder=0
        prefix_map={0:1}
        for i in range(0,n):
            total_sum+=nums[i]
            remainder=total_sum % k
            if remainder < 0:
                remainder=remainder+k
            if remainder in prefix_map:
                result +=prefix_map[remainder]
            prefix_map[remainder]=prefix_map.get(remainder,0)+1
        return result
        