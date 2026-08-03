class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        j = 0
        i = 0
        last_first = 0
        
        while i < len(haystack):

            while j < len(needle) and i < len(haystack) and haystack[i] == needle[j]:
                i += 1
                j += 1

                if i < len(haystack) and not last_first and haystack[i] == needle[0]:
                    last_first = i

            
            if j == len(needle):
                return i - len(needle)
            elif j == 0:
                i += 1
            else:
                if last_first:
                    i = last_first
                    last_first = 0
            j = 0

        return -1 