nums = [4,3,2,7,8,2,3,1]
# nums = [1,1]

def findDisappearedNumbers(nums):
    num_set = set(nums)
    print(num_set)
    res = []
    length = len(nums)
    if length not in num_set : 
        res.append(length)
    for i in range(0,len(nums)):
        if i !=0 and i not in num_set:
            res.append(i)
    return res

print(findDisappearedNumbers(nums))