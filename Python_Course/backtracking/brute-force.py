nums = [1,2]
answer = []

def permutation(nums):
    for i in range(0,len(nums) - 1):
        for j in range(i+1, len(nums)):
            temp_array = nums[i],nums[j] = nums[j],nums[i]
            answer.append(temp_array)
    return answer




print(permutation(nums))
