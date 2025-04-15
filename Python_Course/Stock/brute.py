# Prices = [6,9,2,3,11]

Prices = [9,1,5,3,7,5]

def profit():
    Left_pointer = Prices[0]
    Profit = 0
    for i in range(len(Prices) - 1):
        Right_pointer = Prices[i+1]

        if Left_pointer < Right_pointer :
            temp_profit = Right_pointer - Left_pointer
            if temp_profit > Profit:
                Profit = temp_profit
        else:
            Left_pointer = Right_pointer
    return Profit

if __name__=="__main__":
    result=print(profit())