nums = [-4,-1,0,3,10]


left=0
right=len(nums) - 1

position=len(nums) - 1
new_nums=[0] * len(nums)

while left < right:
    left_square = nums[left] ** 2

    right_square = nums[right] ** 2

    if left_square > right_square:
        new_nums[position]=left_square
        left += 1
    else:
        new_nums[position]=right_square
        right -= 1
    
    position -= 1

print(new_nums)



