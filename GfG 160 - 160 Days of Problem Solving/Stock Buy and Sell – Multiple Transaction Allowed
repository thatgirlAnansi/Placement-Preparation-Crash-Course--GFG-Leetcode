def maxProfit(prices):
    n = len(prices)
    if n <= 1:
        return 0

    max_profit = 0
    for i in range(1, n):
        # Add profit if the price is increasing
        if prices[i] > prices[i - 1]:
            max_profit += prices[i] - prices[i - 1]

    return max_profit
