haystack = "butsad"
needle = "sad"


def index_of_first_occurence(haystack, needle):
    m = len(haystack)
    n = len(needle)
    for i in range(len(haystack) - len(needle) +1):
        if haystack[i:i+n] == needle:
            return i
    return -1    


    

print(index_of_first_occurence(haystack, needle))