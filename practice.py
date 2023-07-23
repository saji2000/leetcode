class Solution:
    def maxProfit(self, prices):
        l, r = 0, 0
        max_profit = 0

        for i in prices:
            profit = prices[r] - prices[l]
            if profit < 0:
                l = r
            r += 1
            max_profit = max(max_profit, profit)

        return max_profit
