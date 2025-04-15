array = [1,2,3,4,5]
k = 3

def reverse(array,left,right):
    while left < right:
        array[left],array[right] = array[right],array[left]
        left += 1
        right -= 1
    return array


def rotate_array(array,k):
    k = k % len(array)
    
    reverse(array,0,len(array) - 1)

    reverse(array, 0, k-1)

    reverse(array, k, len(array) - 1)

    return array

print(rotate_array(array,k))

        

        