class Solution:
    def maxProfit(self, prices):
        l, r = 0
        profit = 0
        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
            profit = max(profit, prices[r] - prices[l])
            r += 1
        return profit
