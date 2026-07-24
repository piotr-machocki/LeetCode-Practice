class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        ans = []

        def backtrack(current_str, open_count, close_count):

            # Base Case
            
            if open_count + close_count == n*2:
                ans.append(current_str)

            if open_count < n:
                backtrack(current_str + "(", open_count+1, close_count)

            if close_count < open_count:
                backtrack(current_str + ")", open_count, close_count+1)
        
        backtrack("", 0, 0)

        return ans