class Solution:
    def longestValidParentheses(self, s: str) -> int:

        left = right = max_len = 0
        
        for char in s:

            if char == "(":
                left += 1
            else:
                right += 1
            
            if left == right:
                max_len = max(max_len, 2*right)
            
            if right > left:
                left = 0
                right = 0
        
        left = right = 0

        for char in reversed(s):

            if char == "(":
                left += 1
            else:
                right += 1
            
            if left == right:
                max_len = max(max_len, 2*left)
            
            if left > right:
                left = 0
                right = 0

        return max_len
            