class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n=len(nums)
        total_zero=0
        total_one=0
        result=0
        difference=0
        prefix_map={0:-1}
        for i in range(0,n):
            if nums[i]==0:
                total_zero+=1
            else:
                total_one+=1
            difference=total_zero-total_one
            if difference in prefix_map:
                result=max(result,i-prefix_map[difference])
                continue
            else:
                prefix_map[difference]=i
        return result


        