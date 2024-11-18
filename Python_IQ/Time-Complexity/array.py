array_list=[3,1,1,7,5,10,2]

sequence=[1,6]


def array_sequence():
    seq_index=0
    for num in array_list:
        print(num)
        if seq_index < len(sequence) and num==sequence[seq_index]:
            seq_index+=1

        if seq_index == len(sequence):
           return True
    else:
        return False



if __name__=="__main__":
    print(array_sequence())
