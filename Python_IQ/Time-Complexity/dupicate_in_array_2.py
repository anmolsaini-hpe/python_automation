
array=[1,2,3,4,5,6,7,1]

duplicate_array=[]

array_2=[]


def duplicate():
    for num in array:
        if num in array_2:
            duplicate_array.append(num)
        else:
            array_2.append(num)

    print(array_2)
    print(duplicate_array)

if __name__=="__main__":
    duplicate()