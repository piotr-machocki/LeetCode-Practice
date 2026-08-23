class Solution:
    def longestValidParentheses(self, s: str) -> int:

        dp = []

        for i in range(len(s)):

            if s[i] == "(":
                dp.append(0)
            else:
                if i == 0:
                    dp.append(0)
                elif s[i - 1] == '(':
                    if i >= 2:
                        dp.append(2 + dp[i - 2])
                    else:
                        dp.append(2)
                else:
                    j = i - dp[i-1] - 1

                    if j >= 0 and s[j] == "(":
                        if j > 0:
                            dp.append(dp[i - 1] + 2 + dp[j - 1])
                        else:
                            dp.append(dp[i - 1] + 2)
                    else:
                        dp.append(0)

        return max(dp, default=0)