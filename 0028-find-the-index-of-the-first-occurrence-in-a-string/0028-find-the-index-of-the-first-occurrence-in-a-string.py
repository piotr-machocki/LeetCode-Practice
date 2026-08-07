class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        # KMP Algorithm

        # Computing LPS Array

        LPS = [0] * len(needle)
        i = 1
        prevLPS = 0

        while i < len(needle):

            if needle[i] == needle[prevLPS]:
                prevLPS += 1
                LPS[i] = prevLPS
                i += 1
            else:
                if prevLPS:
                    prevLPS = LPS[prevLPS - 1]
                else:
                    LPS[i] = 0
                    i += 1

        # traversing the text (haystack)

        h_ptr = 0
        n_ptr = 0

        while h_ptr < len(haystack):

            if haystack[h_ptr] == needle[n_ptr]:
                h_ptr += 1
                n_ptr += 1

                if n_ptr == len(needle):
                    return h_ptr - len(needle)
            else:
                if n_ptr:
                    n_ptr = LPS[n_ptr - 1]
                else:
                    h_ptr += 1

        return -1

