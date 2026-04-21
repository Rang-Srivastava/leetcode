class Solution:
    def reverseString(self, s: List[str]) -> None:
  
        res = []
        stack_one = []
        n = len(s)

        # push into stack
        for i in range(n):
            stack_one.append(s[i])

        # pop from stack
        while stack_one:
            c = stack_one.pop()
            res.append(c)

        # copy back to s (in-place)
        for i in range(n):
            s[i] = res[i]
        
        
        