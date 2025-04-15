# Input = [1,2,5,7,9,11,14]
Input = [2, 7, 11, 15]
Target = 9
Number2 = 0
Number1 = 0

def twosum(Input,Target):
    for i in range(len(Input)):
        Number2 = Target - Input[i]
        if Number2 in Input:
            Number1 = Input[i]
            break
    Number1_index = Input.index(Number1) + 1 
    Number2_index = Input.index(Number2) + 1
    return [Number1_index,Number2_index]

if __name__ == "__main__":
    result=twosum(Input,Target)
    print(result)