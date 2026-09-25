class Solution:
    def countAndSay(self, n: int) -> str:

        ans = ["1"]
        ans_next = []

        for i in range(1, n):

            j = 0

            while j < len(ans):

                num = ans[j]
                num_count = 0

                while j < len(ans) and ans[j] == num:
                    num_count += 1
                    j += 1
                
                ans_next.append(str(num_count))
                ans_next.append(num)
            
            ans = ans_next
            ans_next = []
        
        return "".join(ans)
        




                
