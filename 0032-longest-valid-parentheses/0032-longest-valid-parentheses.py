class Solution:
    def longestValidParentheses(self, s: str) -> int:

        left = 0
        right = 0
        max_len = 0
        
        for i in range(len(s)):

            if s[i] == "(":
                left += 1
            else:
                right += 1
            
            if left == right:
                max_len = max(max_len, 2*right)
            
            if right > left:
                left = 0
                right = 0
        
        left = 0
        right = 0

        for i in range(len(s) - 1, -1, -1):

            if s[i] == "(":
                left += 1
            else:
                right += 1
            
            if left == right:
                max_len = max(max_len, 2*left)
            
            if left > right:
                left = 0
                right = 0

        return max_len
            