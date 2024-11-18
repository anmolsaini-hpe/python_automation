
list_of_char=set()
duplicate_char=[]

def unique_char():
    str = input("Enter a string: ")
    str = str.lower()
    print(str)
    for char in str:
        if char in list_of_char:
            duplicate_char.append(char)
        else:
            list_of_char.add(char)
    
    print(duplicate_char)







if __name__=="__main__":
    unique_char()