class Solution:
    def cuttingRope(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[1] = 1
        for i in range(2,n+1):
            for j in range(1,i//2+1):
                dp[i] = max(dp[i],max(j,dp[j])*max(i-j,dp[i-j]))
        return dp[-1]

# https://leetcode-cn.com/problems/jian-sheng-zi-lcof/solution/shu-xue-zhi-shi-he-dong-tai-gui-hua-liang-chong-fa/