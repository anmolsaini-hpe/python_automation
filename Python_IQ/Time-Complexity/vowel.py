
def check_vowel(string):
    vowels=["a","e","i","o","u"]
    new_list=[]
    for i in string:
        if i in vowels:
            new_list.append(i)
    print("Here are the vowels in the string",new_list)





if __name__=="__main__":
    string=str(input("Enter the string "))
    check_vowel(string)
