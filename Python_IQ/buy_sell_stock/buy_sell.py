prices = [7,1,5,3,6,4]
# prices = [7,6,4,3,1]
# prices = [2,4,1]

sorted_prices=sorted(prices)

# print(sorted_prices)
buy_price=sorted_prices[0]
# print(buy_price)
buy_price_index=prices.index(buy_price)
# print(buy_price_index)
new_prices=[]
# # print(buy_price_index)
# # print(len(prices))

for i in range(len(prices)):
    new_prices.append(prices[i]-buy_price)
print(new_prices)
sorted_new_prices=sorted(new_prices)
print(sorted_new_prices)
if len(sorted_new_prices) == 0:
    profit=0
    print(profit)
else:
    profit = sorted_new_prices[len(sorted_new_prices)-1]
    print(profit)

# print(profit)