s = "   the sky  is blue  "

def reverse_words(s):

    s = s.strip()
    left = len(s) - 1
    right = len(s) - 1
    result = []
    
    while left >= 0:
        while left >= 0 and s[left] != " ":
            left -= 1
        result.append(s[left + 1:right + 1])
        
        while left >=0 and s[left] == " ":
            left -= 1
        
        right = left

    return " ".join(result)
    

print(reverse_words(s))





# s = "   the sky  is blue  "
# result = []
# def reverse_words(s):
#     result = s.split()
#     return " ".join(result[::-1])

# print(reverse_words(s))