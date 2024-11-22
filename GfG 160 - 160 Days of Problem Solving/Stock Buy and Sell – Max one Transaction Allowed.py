class Solution:
    def maximumProfit(self, prices):
        if not prices or len(prices) < 2:
            return 0

        min_price = float('inf')
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
    
        return max_profit
