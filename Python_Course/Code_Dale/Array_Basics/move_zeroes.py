# nums = [0,1,0,3,12]
nums = [1,2,0,4,9]

def moveZeroes(nums):
    pointer  = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i],nums[pointer] = nums[pointer],nums[i]
            pointer += 1
    return nums



print(moveZeroes(nums))