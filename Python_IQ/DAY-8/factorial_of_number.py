
def factorial(number):
    factor=1
    for i in range(1,number+1):
        factor=factor*i
    print("Factor of number is",factor)



if __name__=="__main__":
    number=int(input("Enter the number "))
    factorial(number)