def stock_picker(prices):
    """Return best day to buy and to sell stocks.

    :param prices: List of prices of stock at each day
    :return days: List containing the best day to buy, and the best
    day to sell the stocks
    """
    days = []

    if len(prices) < 2:
        return days

    max_profit = 0
    num_days = len(prices)
    for i in range(0, num_days):
        for j in range(i, num_days):
            profit = prices[j] - prices[i]
            if profit > max_profit:
                max_profit = profit
                days = [i, j]

    return days
