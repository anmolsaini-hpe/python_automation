s = "GAAAATCCCCGAAAATCCCCGAAAAAGGGTTT"

def findRepeatedSequence(s):
    L = 10
    n = len(s)
    seen = set()
    output = set()

    for start in range(0,n-L+1):
        temp = s[start:start+L]
        if temp in seen:
            output.add(temp)
        else:
            seen.add(temp)

    return list(output)

print(findRepeatedSequence(s))