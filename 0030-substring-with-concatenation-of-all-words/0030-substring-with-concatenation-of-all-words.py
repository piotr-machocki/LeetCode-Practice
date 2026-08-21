class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        word_target = {}
        word_count = {}
        sol = []
        
        for i in range(len(words)):

            if words[i] in word_target:
                word_target[words[i]] += 1
            else:
                word_target[words[i]] = 1
        
        word_len = len(words[0])
        i = 0
        target = 0

        while i < word_len:

            L = i
            P = L + word_len

            while P <= len(s):

                candidate = s[P-word_len:P]

                if candidate in word_target:
                    if candidate in word_count:
                        word_count[candidate] += 1
                    else:
                        word_count[candidate] = 1

                    if not (word_count[candidate] > word_target[candidate]):
                        target += 1

                    while word_count[candidate] > word_target[candidate]:

                        word_drop = s[L:L+word_len]
                        word_count[word_drop] -= 1

                        if word_count[word_drop] < word_target[word_drop]:
                            target -= 1
                        
                        if word_count[word_drop] == 0:
                            del word_count[word_drop]
                        
                        L += word_len

                    if target == len(words):

                        sol.append(P - len(words)*word_len)

                        word_drop = s[L:L+word_len]

                        if word_count[word_drop] == 1:
                            del word_count[word_drop]
                        else:
                            word_count[word_drop] -= 1
                        
                        target -= 1
                        L += word_len
                
                    P += word_len     

                else:
                    L = P 
                    P += word_len
                    word_count = {}
                    target = 0

            i += 1
            word_count = {}
            target = 0
        
        return sol