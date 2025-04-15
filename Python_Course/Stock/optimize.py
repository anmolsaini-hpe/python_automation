prices = [9,1,5,3,7,5]

def maxProfy(prices):
    left = 0
    profit = 0
    for right in range(1,len(prices)):
        if prices[left] < prices[right]:
            profit = max(profit, prices[right] - prices[left])
        else:
            left = right

    return profit