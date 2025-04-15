# prices = [9,1,5,3,7,5]

prices = [9,2,5,3,1,5]


def maxProfit(prices):
    left = 0
    right = 1
    profit = 0
    while right < len(prices):
        left_price = prices[left]
        right_price = prices[right]

        if  left_price < right_price:
            temp_profit = right_price - left_price
            if temp_profit > profit:
                profit = temp_profit
        else:
            left = right
        right += 1
    return profit

print(maxProfit(prices))