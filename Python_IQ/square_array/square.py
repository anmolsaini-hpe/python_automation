nums = [-4,-1,0,3,10]
new_nums=[]

def square_array():
    for i in nums:
        new_nums.append(i*i)
    return sorted(new_nums)

if __name__=="__main__":
    result=square_array
    