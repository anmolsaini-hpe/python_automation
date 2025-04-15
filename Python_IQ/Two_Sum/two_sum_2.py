# nums = [2,7,11,15]
# target = 9

nums = [3,2,4]
target = 6

num_to_index={}

for i,num in enumerate(nums):
    
    complacent = target - num

    if complacent in num_to_index:
        print([num_to_index[complacent],i])
    else:
        num_to_index[num]=i
        # print(num_to_index)

