

def primenumber():
    for i in range(first_interval,second_interval):
        for j in range(2,i):
            if i%j==0:
                print(i, "number is not prime")
                break
        else:
            print(i, "Number is prime")



if __name__=="__main__":
    first_interval=int(input("Enter the first interval "))
    second_interval=int(input("Enter the second interval "))

    if (first_interval > 1 and second_interval > 2) and (first_interval < second_interval):
        primenumber()
    else:
        print("Enter the valid range !")