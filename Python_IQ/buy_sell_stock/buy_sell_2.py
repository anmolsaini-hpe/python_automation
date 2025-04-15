# prices = [7,1,5,3,6,4]
prices = [2,4,1]
max_profit=0

for i in range(len(prices)):
    for j in range(i+1, len(prices)):
        profit=prices[j] - prices[i]
        max_profit=max(max_profit,profit)
        print(max_profit)
print(max_profit) 
