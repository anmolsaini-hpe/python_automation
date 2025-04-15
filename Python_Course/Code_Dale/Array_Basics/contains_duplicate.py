nums = [1,2,3,4]

def contains_duplicate(nums):
    ht = {}
    for i in range(len(nums)):
        if nums[i] in ht:
            return True
        else:
            ht[nums[i]] = i
            print(ht)
    return False

                   



print(contains_duplicate(nums))
