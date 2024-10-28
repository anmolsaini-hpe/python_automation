# https://www.youtube.com/watch?v=umLYEPmjCNI&list=PL8WTXLSrtyWpXqqGzbkQySC43rgU38htm&index=3

input_of_number=int(input("Enter the number "))

list_of_numbers=[]

def numbers_list():
    for i in range(0, input_of_number):
        list_of_numbers.append(i)
    return list_of_numbers

def average():
    list=numbers_list()
    length_of_list=len(list)
    sum=0
    for j in list:
        sum=sum+j
    average_of_numbers=float(sum/length_of_list)
    print("Average of number ", average_of_numbers)


if __name__ =="__main__":
    average()