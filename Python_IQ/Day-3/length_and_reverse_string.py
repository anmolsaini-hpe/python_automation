Str="anmol"
def lenght_of_string():
    lenght_of_string=0
    for i in Str:
        lenght_of_string=lenght_of_string+1
    print("Length of String :",lenght_of_string)


def reverse_of_string():
    new_str=""
    for i in Str:
        new_str=i+new_str
    print("Reverse of string :", new_str)


if __name__=="__main__":
    lenght_of_string()
    reverse_of_string()