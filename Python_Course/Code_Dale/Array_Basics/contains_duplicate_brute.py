nums = [1,2,3,1]

def contains_duplicate(nums):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] == nums[j]:
                return True
    return False


print(contains_duplicate(nums))
