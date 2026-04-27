class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        stack = []

        for i in range(n):
            # if opening bracket, push into stack
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
                continue

            # if closing bracket and stack is empty
            if not stack:
                return False

            # if matching closing bracket with stack top
            if s[i] == ')' and stack[-1] == '(':
                stack.pop()
            elif s[i] == '}' and stack[-1] == '{':
                stack.pop()
            elif s[i] == ']' and stack[-1] == '[':
                stack.pop()
            else:
                return False

        # after loop, stack should be empty
        if stack:
            return False

        return True