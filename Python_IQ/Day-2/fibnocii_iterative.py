# Fibonacci Series in Python | With Recursion | Python Interview Questions for DevOps | 02
# https://www.youtube.com/watch?v=dT7_twUuJcQ&list=PL8WTXLSrtyWpXqqGzbkQySC43rgU38htm&index=4

#Expectation : [0,1,1,2,3,5,8,13,21,34]

number=int(input("Enter the index till you want fibonnaci series "))

fibonaaci_series=[]

def testfunc():
    first_num=0
    second_num=1
    third_number=0
    fibonaaci_series.append(first_num)
    fibonaaci_series.append(second_num)

    for i in range(0,number):
        third_number=first_num+second_num
        first_num=second_num
        second_num=third_number
        fibonaaci_series.append(third_number)
    print(fibonaaci_series)


if __name__=="__main__":
    testfunc()