

def occurence(string,char):
    count=0
    for i in range(0,len(string)):
        print(string[i])
        if char==string[i]:
            count+=1
    print(char,"occurs in the string for", count, "times")






if __name__=="__main__":
    string=str(input("Enter the string "))
    char=str(input("Enter the character "))
    occurence(string,char)