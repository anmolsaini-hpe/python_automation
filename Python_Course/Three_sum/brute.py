nums=[4, 7, 4, -1, -3]

def threenumbs(num):
    nums.sort()
    res = []
    for i in range(len(nums)):
        if i==0 or nums[i] != nums[i-1]:
            left = i + 1 
            right = len(nums) - 1

            while left < right:
                sum = num[i] + num[left] + num[right]

                if sum == 0:
                    res.append([num[i], num[left], num[right]])
                    left += 1
                    if num[left] == num[left -1]:
                        left += 1
                elif sum < 0:
                    left += 1
                    if num[left] == num[left -1]:
                        left += 1
                else:
                    right -= 1
    
    return res



result = threenumbs(nums)
print(result)