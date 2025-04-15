string = "pqbrstbuvwpvy"
def longest_substring_with_uniq_char(string):
    start = 0
    max_len = 0
    seen = {}
    for i in range(len(string)):
        char = str[i]
        if char in seen:
            start = max(start, seen[char] + 1)
        max_len = max(max_len, i-start+1)
        seen[char] = i
    return max_len


print(longest_substring_with_uniq_char(string))