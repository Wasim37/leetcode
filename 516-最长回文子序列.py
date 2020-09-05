# 要点：在子串s[i..j]中，最长回文子序列的长度为dp[i][j]
# 想求dp[i][j]需要知道dp[i+1][j-1]，dp[i+1][j]，dp[i][j-1]这三个位置的值
# 利用2个指针，从2头往中间扫。

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1

        # print(dp)
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                # 核心
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j])
        return dp[0][n-1]
