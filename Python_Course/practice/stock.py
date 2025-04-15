# prices = [9,1,5,3,7,5]
prices = [7,2,5,3,1,4,6]
# prices = [7,6,4,3,1]

def stocks(prices):
    max_profit = 0
    left = 0
    right = 1
    while right <= len(prices) -1:
        if prices[left] < prices[right]:
            temp_profit = prices[right] - prices[left]
            max_profit = max(max_profit,temp_profit)
            right += 1
        else:
            left = right
            right += 1
    
    return max_profit


print(stocks(prices))