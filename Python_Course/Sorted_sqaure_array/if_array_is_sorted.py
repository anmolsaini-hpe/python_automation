def sorted_array(array):
    x=0
    y=len(array) - 1
    new_array=[0]*len(array)
    

    for i in reversed(range(len(array))):
        square_x = array[x] ** 2
        square_y = array[y] ** 2
        if square_x >= square_y:
            new_array[i] = square_x
            x = x + 1
        elif square_x <= square_y:
            new_array[i] = square_y
            y = y - 1
    print(new_array)


sorted_array([-5,-4,-2,1,3,11])