def two_sum(array,target):
    for i in range(0,len(array)-1):
        for j in range(i+1,len(array)):
            if array[i]+array[j]==target:
                return(i,j)
    return []






if  __name__=="__main__":
    array = [2, 7, 3, -1, 15]
    target = 2
    result=two_sum(array,target)
    print(result)