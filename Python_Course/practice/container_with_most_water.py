# array = [1, 5, 6, 3, 4]

array = [3, 7, 5, 6, 8, 4]

def container_with_most_water(array):
    max_area = float('-inf')
    left = 0
    right = len(array) - 1

    while left < right:
        area = min(array[left], array[right]) * (right - left)
        max_area = max(max_area, area)
        if array[left] < array[right]:
            left += 1
        else:
            right -= 1
    return max_area

print(container_with_most_water(array))