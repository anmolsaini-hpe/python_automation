array = [3, 7, 5, 6, 8, 4]

def container(array):
    left_pointer = 0                  
    right_pointer = len(array) - 1
    max_area = 0

    while left_pointer < right_pointer:
        temp_area = min(array[left_pointer], array[right_pointer]) * (right_pointer - left_pointer)
        max_area = max(temp_area,max_area)
        if array[left_pointer] < array[right_pointer]:
            left_pointer +=1
        else:
            right_pointer -=1
    
    return(max_area)



print(container(array))