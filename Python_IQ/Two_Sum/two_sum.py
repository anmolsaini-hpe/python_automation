nums = [2,7,11,15] 
target = 9
new_list=[]

def two_sum():
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                # print(nums[i],nums[j])
                new_list.append(i)
                new_list.append(j)
                return new_list

x=two_sum()
print(x)