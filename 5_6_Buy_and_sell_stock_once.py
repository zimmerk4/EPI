def buy_and_sell_stock_once(prices):
    min_so_far = float('inf')
    max_profit = 0
    for price in prices:
        sell_now = price - min_so_far
        max_profit = max(sell_now, max_profit)
        min_so_far = min(min_so_far, price)
    return max_profit
