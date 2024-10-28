
def prime_number():
    for i in range(2,number):
        if number%i==0:
           print("Number is not prime number")
           break
    else:
        print("Number is prime number")


if __name__=="__main__":
    number=int(input("Enter the number: "))
    if number < 1:
        print("Enter the correct number")
    else:
        prime_number()