class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        word_len = len(words[0])
        target_count = {}
        sol = []

        # Runtime: O(len(words))    
        # Memory: O(len(words))

        for i in range(len(words)):
            if words[i] not in target_count:
                target_count[words[i]] = 1
            else:
                target_count[words[i]] += 1

        seen_count = {}

        L = 0
        P = len(words) * word_len
        i = 0

        while P <= len(s):

            edge = L+i+word_len

            if edge <= P:

                candidate = s[L+i:edge]

                if candidate in target_count:
                    if candidate in seen_count:
                        seen_count[candidate] += 1
                    else:
                        seen_count[candidate] = 1
                    i += word_len
                else:
                    L += 1
                    P += 1
                    i = 0
                    seen_count = {}
            else:
                count = True

                for item in seen_count.items():

                    if target_count[item[0]] == item[1]:
                        continue
                    else:
                        count = False
                        break

                
                if count:
                    sol.append(P - (len(words) * word_len))
                
                L += 1
                P += 1
                i = 0
                seen_count = {}

        return sol       


        

