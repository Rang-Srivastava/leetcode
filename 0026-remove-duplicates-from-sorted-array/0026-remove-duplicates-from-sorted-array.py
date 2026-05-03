class  Solution:
    def removeDuplicates(self,nums:List[int])->List[int]:
        n=len(nums)
        i=0
        j=1
        unique_element=1
        for i in range(n):
            while j<n:
                if nums[j]==nums[j-1]:
                    j+=1
                else:
                    nums[i+1]=nums[j]
                    i+=1
                    j+=1
                    unique_element+=1
        return unique_element

        