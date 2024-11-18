
def perfect_number(number):
    list_of_numbers=[]
    sum_of_numbers=0
    for i in range(1,number):
        if (number%i==0):
            list_of_numbers.append(i)
    print(list_of_numbers)
    
    for j in list_of_numbers:
        sum_of_numbers=sum_of_numbers+j
    print(sum_of_numbers)
    
    if sum_of_numbers==number:
        print(number,"is a perfect number")
    else:
        print(number,"is not a perfect number")






if __name__=="__main__":
    number=int(input("Enter the number "))
    perfect_number(number)