number=int(input("Enter the number: "))

def leap_year():
    if (number%400==0) | (number%100!=0) and (number%4==0):
             print("It is a leap year")
    else:
            print("It is NOT leap year")

if __name__=="__main__":
    leap_year()
