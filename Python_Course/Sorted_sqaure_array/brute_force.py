def sorted_squared(array):
    #write code here.make sure to return desired array
    new_array=[]
    if array==0:
        return array
    else:
        for num in array:
            new_array.append(num**2)
        return sorted(new_array)