# 记录【今天之前买入的最小值】
# 计算【今天之前最小值买入，今天卖出的获利】，也即【今天卖出的最大获利】
# 比较【每天的最大获利】，取最大值即可

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = float('inf')
        maxprofit = 0
        for price in prices:
            minprice = min(minprice, price)
            maxprofit = max(maxprofit, price - minprice)
        return maxprofit