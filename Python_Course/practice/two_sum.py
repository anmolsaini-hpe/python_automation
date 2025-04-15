nums = [1, 3, 4]
target = 5
nums = [2,7,11,15] 
target = 9

# Two pointer is useful technique for two sum if and only array is sorted.
# nums = [3,2,4]
# target = 6

def two_sum(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right :
        sum = nums[left] + nums[right]
        if sum == target:
            return [left, right]
        elif sum < target:
            left += 1
        else:
            right -=1
    return []


print(two_sum(nums, target))