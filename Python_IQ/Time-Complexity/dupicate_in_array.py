
array=[1,2,3,4,5,6,7,1]

duplicate_array=[]

def duplicate():
    for i in range(0, len(array)):
        # print(array[i])
        for j in range(i+1,len(array)):
            # print(array[j])
            if array[i]==array[j]:
                # print(array[i])
                duplicate_array.append(array[i])
    print(duplicate_array)




if __name__=="__main__":
    duplicate()