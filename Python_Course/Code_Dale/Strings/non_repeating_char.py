# s = "abAA1ac"
# s = "abaRb150"
# def non_repeating_char(s):
#     for i in range(0,len(s)):
#         repeat = False
#         for j in range(len(s)):
#             # print(s[i],s[j])
#             if i!=j and s[i] == s[j]:
#                 repeat = True
#         if repeat == False:
#             return s[i]

# print(non_repeating_char(s))



# s = "abAA1ac"
s = "abaRb150"
def non_repeating_char(s):
    ht = {}
    for i in range(0,len(s)):
        if s[i] in ht:
            ht[s[i]] += 1
        else:
            ht[s[i]] = 1
    print(ht)
    for i in range(0,len(ht)):
        if ht[s[i]] == 1:
            return i
print(non_repeating_char(s))