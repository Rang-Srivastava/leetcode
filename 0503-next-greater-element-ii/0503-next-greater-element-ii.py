class Solution:
    def nextGreaterElements(self, nums):
        n = len(nums)
        res = [-1] * n
        stack = []

        # 🔹 IMAGE PART 1: stack ko right se prepare karna
        for i in range(n-1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()
            stack.append(i)

        # 🔹 IMAGE PART 2: actual answer fill karna
        for i in range(n-1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()

            if stack:
                res[i] = nums[stack[-1]]

            stack.append(i)

        return res