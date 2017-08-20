import timeit


def buy_and_sell_stock_twice(prices):
    # Not the code from the book. This algorithm does the same but without additional space. Runs slightly faster too
    max_first_profit = 0
    max_second_profit = 0
    min_price_so_far = float('inf')
    max_price_so_far = float('-inf')
    first_sell_index = 0
    second_buy_index = len(prices)
    max_total_profit = 0
    for i in range(len(prices) // 2):
        sell_now = prices[i] - min_price_so_far
        min_price_so_far = min(min_price_so_far, prices[i])
        if sell_now > max_first_profit:
            max_first_profit = sell_now
            first_sell_index = i
        max_first_profit = max(max_first_profit, prices[i] - min_price_so_far)

    for i in reversed(range(len(prices) // 2, len(prices))):
        sell_now = max_price_so_far - prices[i]
        max_price_so_far = max(max_price_so_far, prices[i])
        if sell_now > max_second_profit:
            max_second_profit = max_price_so_far - prices[i]
            second_buy_index = i
            
    if max_first_profit < max_second_profit:
        min_price_so_far = float('inf')
        for i in range(second_buy_index):
            sell_now = prices[i] - min_price_so_far + max_second_profit
            max_total_profit = max(sell_now, max_total_profit)
            min_price_so_far = min(min_price_so_far, prices[i])
            
    elif max_first_profit > max_second_profit:
        max_price_so_far = float('-inf')
        for i in reversed(range(first_sell_index + 1, len(prices))):
            sell_now = max_price_so_far - prices[i] + max_first_profit
            max_total_profit = max(sell_now, max_total_profit)
            max_price_so_far = max(max_price_so_far, prices[i])

    else:
        max_total_profit = max_first_profit + max_second_profit

    return max_total_profit


def book_version(prices):
    max_total_profit, min_price_so_far = 0, float('inf')
    first_buy_sell_profits = [0] * len(prices)
    for i, price in enumerate(prices):
        min_price_so_far = min(min_price_so_far, price)
        max_total_profit = max(max_total_profit, price - min_price_so_far)
        first_buy_sell_profits[i] = max_total_profit
    max_price_so_far = float('-inf')
    for i, price in reversed(list(enumerate(prices[1:], 1))):
        max_price_so_far = max(max_price_so_far, price)
        max_total_profit = max(max_total_profit, max_price_so_far - price + first_buy_sell_profits[i -1])
    return max_total_profit


A = [12, 11, 13, 3, 9, 12, 8, 20, 14, 13, 15]
print(buy_and_sell_stock_twice(A))
print(book_version(A))
print(timeit.timeit('buy_and_sell_stock_twice([12, 11, 13, 9, 12, 8, 14, 13, 15])', globals=globals()))
print(timeit.timeit('book_version([12, 11, 13, 9, 12, 8, 14, 13, 15])', globals=globals()))
