array=[1, 2, 0, 4, 3, 0, 5, 0]

zero_array=[]
new_array=[]

def move_zero():
    for num in array:
        if num == 0:
            zero_array.append(num)
        else:
            new_array.append(num)
    final_array = new_array + zero_array
    print(final_array)



if __name__=="__main__":
    move_zero()
