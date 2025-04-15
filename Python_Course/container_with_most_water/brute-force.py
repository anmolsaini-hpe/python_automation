# array = [1,2,6]
array = [3,7,5,6,8,4]

def container(array):
    area = 0
    for i in range(0, len(array) -1):
        for j in range(i+1, len(array)):
            temp_area = min(array[i],array[j]) * (j-i)
            area = max(temp_area, area)
    return area



print(container(array))