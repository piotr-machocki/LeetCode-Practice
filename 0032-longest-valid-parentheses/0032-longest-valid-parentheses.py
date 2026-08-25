class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        stack = []
        max_len = 0

        stack.append(-1)

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    max_len = max(i - stack[-1], max_len)  
                else:
                    stack.append(i)
        
        return max_len