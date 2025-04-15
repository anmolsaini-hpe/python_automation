nums = [-7,-3,2,3,11]

def sorted_sqaure(nums):
    new_nums = [0] * len(nums)
    left = 0
    right = len(nums) -1
    position = len(nums) - 1

    while left <= right :
        left_square = nums[left] ** 2
        right_square = nums[right] ** 2
    
        if right_square > left_square :
            right -= 1
            new_nums[position] = right_square
        else:                                   # This covers both the cases i.e. when left_square > right_sqaure and left_square == right_square
            left += 1
            new_nums[position] = left_square
        
        position -= 1
    return new_nums

result = sorted_sqaure(nums)
print(result)