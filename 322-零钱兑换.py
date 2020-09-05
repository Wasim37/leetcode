
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # float('inf') 代表正无穷大
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            # print('coin:', coin)
            for x in range(coin, amount + 1):
                # print('x:', x, ',', dp[x], ',', dp[x - coin] + 1)
                dp[x] = min(dp[x], dp[x - coin] + 1)
            # print(dp)
        return dp[amount] if dp[amount] != float('inf') else -1