class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        j = 0
        
        for i in range(len(haystack)):

            while j < len(needle) and i < len(haystack) and haystack[i] == needle[j]:
                i += 1
                j += 1
            
            if j == len(needle):
                return i - len(needle)
            else:
                j = 0

        return -1 