class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) % 2 == 1:
            return False

        paren = 0
        curly = 0
        square = 0

        match_up = {"(" : ")", "{" : "}", "[" : "]"}

        LIFO = []

        for i in range(len(s)):
            
            if s[i] in match_up:

                if i + 1 < len(s) and s[i+1] in match_up.values() and match_up[s[i]] != s[i+1]:
                    return False

                elif s[i] == "(":
                    paren += 1
                    LIFO.append("(")
                
                elif s[i] == "{":
                    curly += 1
                    LIFO.append("{")

                elif s[i] == "[":
                    square += 1
                    LIFO.append("[")

            
            else:
                if len(LIFO) > 0 and match_up[LIFO[(len(LIFO) - 1)]] == s[i]:

                    LIFO.pop()

                    if s[i] == ")":
                        if paren:
                            paren -= 1
                        else:
                            return False

                    if s[i] == "}":
                        if curly:
                            curly -= 1
                        else:
                            return False
                    
                    if s[i] == "]":
                        if square:
                            square -= 1
                        else:
                            return False
                else:
                    return False

        if paren + curly + square == 0:
            return True
        else:
            return False