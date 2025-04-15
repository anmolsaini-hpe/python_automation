# nums = [5,4,-1,7,8]
# nums = [1,2,3,4,5]
# nums = [-2,1,-3,4,-1,2,1,-5,4]
# nums = [1,2,-10,3,9]
# nums = [1]
nums = [-1]

def max_subarray(nums):
    curr_sum = 0
    max_sum = float('-inf')
    for i in range(len(nums)):
        curr_sum = max(nums[i],curr_sum + nums[i])
        max_sum = max(max_sum,curr_sum)
    return max_sum


print(max_subarray(nums))