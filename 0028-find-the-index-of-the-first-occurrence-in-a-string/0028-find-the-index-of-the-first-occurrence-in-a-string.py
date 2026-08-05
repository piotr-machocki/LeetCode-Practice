class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        j = 0

        for i in range(len(haystack)):
            
            while i < len(haystack) and j < len(needle) and haystack[i] == needle[j]:
                j += 1
                i += 1
            
            if j == len(needle):
                return i - j
            else:
                j = 0

        return -1