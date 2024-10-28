input_number=float(input("Enter the number "))

def check_number():

    if (input_number > 0):
        print("Number is positive")
    elif (input_number < 0):
        print("Numbe is negetive")
    elif (input_number == 0):
        print("Number is Zero")
    

def sum_of_natural_numbers():
    sum = (input_number*(input_number+1))/2
    print("Sum of natural numbers", sum)

if __name__=="__main__":
    check_number()
    sum_of_natural_numbers()