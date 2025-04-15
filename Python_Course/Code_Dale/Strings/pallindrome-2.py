s = "race a car"
s = s.lower()
s = ''.join(e for e in s if e.isalnum())


def pallindrome(s):
    s = s.lower()
    s = ''.join(e for e in s if e.isalnum())
    left = 0
    right = len(s) - 1
    while left <= right :
        if s[left] != s[right]:
            return False
        left +=1
        right -=1
    return True

print(pallindrome(s))