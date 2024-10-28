# Swapping Two Numbers Without Using Third Variable | Python Interview Questions for DevOps | 01
# https://www.youtube.com/watch?v=umLYEPmjCNI&list=PL8WTXLSrtyWpXqqGzbkQySC43rgU38htm&index=3

def swap():
    
    first_number=30
    second_number=20

    print("Before Swap : ", first_number, second_number)

    first_number=first_number+second_number #50

    second_number=first_number-second_number #30

    first_number=first_number-second_number #20

    print("After Swap : ", first_number, second_number)

swap()
