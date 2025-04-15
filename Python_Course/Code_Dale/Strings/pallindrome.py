str = "malayalam"


def pallindrome(str):
    left = 0
    right = len(str) - 1
    while left <= right :
        if str[left] != str[right]:
            return False
        left +=1
        right -=1
    return True

print(pallindrome(str))

# def pallindrome(str):
#     str2 = ""
#     for i in str[::-1]:
#         str2 += i
#     if str == str2:
#         return True
#     return False

# print(pallindrome(str))

# def pallindrome(str):
#     str_array = list(str)
#     str2_array = []

#     for i in str_array[::-1]:
#         str2_array.append(i)
#     str2 = ''.join(str2_array)
#     if str == str2 :
#         return True
#     return False
    


# print(pallindrome(str))