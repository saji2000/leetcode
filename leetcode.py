class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit  = 0

        for sell in prices:
            if sell < buy:
                buy = sell
            else:
                profit = max(profit, sell - buy)
        return profit