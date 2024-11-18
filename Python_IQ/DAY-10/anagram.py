

def anagram(str1, str2):
    print(sorted(str1))
    print(sorted(str2))
    if (sorted(str1)) == (sorted(str2)):
        print("It is an anagram")
    else:
        print("It is not anagram")


if __name__=="__main__":
    str1=str(input("Enter the first string "))
    str2=str(input("Enter the second string "))
    anagram(str1, str2)