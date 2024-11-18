
array=[1,2,3,4,5,6,7,1]

duplicate_array=[]

seen = set()


def duplicate():
    for num in array:
        if num in seen:
            duplicate_array.append(num)
        else:
            seen.add(num)

    print(seen)
    print(duplicate_array)

if __name__=="__main__":
    duplicate()