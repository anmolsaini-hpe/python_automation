# nums = [-2, -0, 2, 1, -1, -3]
# nums = [-1, 2, 6, -1, 1]
# nums = [-1,0,1,2,-1,-4]
# nums = [0,1,1]
nums = [0,0,0]
target = 0

def three_sum(nums, target):
    nums.sort()
    res = set()
    for i in range(len(nums)):
        left = i + 1 
        right = len(nums) - 1 

        while left < right : 
            sum = nums[left] + nums[right] + nums[i]
            if sum == target:
                res.add((nums[i], nums[left], nums[right]))
                left +=1
            elif sum < target:
                left += 1
            else:
                right -= 1
    return list(res)

print(three_sum(nums, target))
                