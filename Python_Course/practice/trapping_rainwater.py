array = [3, 0, 1, 0, 4, 0, 2]

def trapping_rainwater(array):
    left = 0
    right = len(array) - 1
    left_max = 0
    right_max = 0
    result = 0

    while left < right:
        left_max = max(left_max,array[left])
        right_max = max(right_max,array[right])

        if left_max <= right_max:
            result += left_max - array[left]
            left += 1
        else:
            result += right_max - array[right]
            right -= 1
    return result

    


print(trapping_rainwater(array))