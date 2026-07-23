class Solution:
    def isValid(self, s: str) -> bool:
        
        matching = {")": "(", "}": "{", "]": "["}

        stack = []

        for char in s:
            if char not in matching:
                stack.append(char)
            else:
                if stack and matching[char] == stack[-1]:
                    stack.pop()
                else:
                    return False

        return not stack
