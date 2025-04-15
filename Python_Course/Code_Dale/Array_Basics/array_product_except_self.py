# nums = [1, 2, 3, 4]
nums = [-1,1,0,-3,3]

def array_product(nums):
    answer = [1] * len(nums)  # Initialize answer array
    left_product = 1
    right_product = 1
    left_pointer = 0
    right_pointer = len(nums) - 1

    while left_pointer < len(nums) : 
        answer[left_pointer] *= left_product
        left_product *= nums[left_pointer]
        left_pointer += 1
        
        answer[right_pointer] *= right_product
        right_product *= nums[right_pointer]
        right_pointer -= 1
    
    return answer
        
print(array_product(nums))
    