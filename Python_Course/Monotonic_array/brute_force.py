def monotonic_array(array):
    first = array[0]
    last = array[len(array) - 1]

    if len(array) == 0:
        return True

    if first > last:
        for i in range(len(array) - 1):
            if array[i] < array[i+1]:
                return False
        #array is MD or NM
    elif first == last:
        for i in range(len(array) - 1):
            if array[i] != array[i+1]:
                return False
        #array is Monotonic if all numbers are same or NM
    else:
        for i in range(len(array) - 1):
            if array[i] > array[i+1]:
                return False
        # first < last and array is MI or NM
    return True

# result = monotonic_array([1,2,3,4,5])
# result = monotonic_array([5,4,3,2,1])
# result=monotonic_array([1,3,2,4])
result=monotonic_array([3,3,3,3])

print(result)