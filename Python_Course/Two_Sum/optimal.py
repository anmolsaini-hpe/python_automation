def two_sum(array,target):
    num_available={}
    for i in range(0,len(array)):
        num_needed=target-array[i]
        if num_needed in num_available:
            return [num_available[num_needed],i]
        else:
            num_available[array[i]]=i
    return []


if  __name__=="__main__":
    array = [2, 7, 3, -1, 15]
    target = 2
    result=two_sum(array,target)
    print(result)