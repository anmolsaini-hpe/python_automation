
list=[]
def reverse_number(number):
    reverse=""
    for i in str(number):
        list.append(i)
    for j in list:
        reverse=j+reverse
    print("Reverse number ",reverse)


if __name__=="__main__":
    number=int(input("Enter the number "))
    reverse_number(number)
