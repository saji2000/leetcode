class Solution:
    def maxProfit(self,prices):
     
        l = 0
        r = 1
        profit = 0
        max_profit = 0 

        while r < len(prices):
            profit = prices[r] - prices[l]

            if profit > 0:
                max_profit = max(profit, max_profit)
            else:
                l = r
            r += 1
        return max_profit