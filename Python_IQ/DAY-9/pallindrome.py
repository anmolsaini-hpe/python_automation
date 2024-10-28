
list1=[]
list2=[]

def pallindrome(number):
    num_str=str(number)
    for i in num_str:
        list1.append(i)
    list2=list1[::-1]
    
    if list1==list2:
        print(number,"is pallindrome")
    else:
        print(number,"is NOT pallindrome")




if __name__=="__main__":
    number=int(input("Enter the number "))
    pallindrome(number)