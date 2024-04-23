class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for buy in range(len(prices)):
            for sell in range(buy + 1, len(prices)):
                profit = max(profit, prices[sell] - prices[buy])
        return profit