# s = "Hello World"
# s = "   fly me   to   the moon  "
s = "luffy is still joyboy"
def length_of_last_word(s):
    length = 0
    right = len(s) - 1

    while right >=0 and s[right] == ' ':
        right -= 1

    while right >=0 and s[right] != ' ':
        length += 1
        right -= 1

    return length

print(length_of_last_word(s))