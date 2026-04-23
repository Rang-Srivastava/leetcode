class Solution:
    def removeDuplicates(self, s: str) -> str:
        n=len(s)
        my_stack=[]
        res=[]
        for i in range(n):
            if not my_stack:
                my_stack.append(s[i])
            elif my_stack[-1]==s[i]:
                my_stack.pop()
            else:
                my_stack.append(s[i])
        while my_stack:
            res.append(my_stack.pop())
        res.reverse()
        return "".join(res)

       
        