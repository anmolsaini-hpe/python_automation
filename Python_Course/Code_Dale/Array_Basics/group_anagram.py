strings = ['arc', 'abc', 'car', 'cat', 'act', 'acb', 'atc']

def group_anagram(strings):
    sorted_strings = [''.join(sorted(e)) for e in strings]
    hash = {}
    for i in range(len(sorted_strings)):
        if sorted_strings[i] in hash:
            hash[sorted_strings[i]].append(strings[i])
        else:
            hash[sorted_strings[i]] = [strings[i]]

    return list(hash.values())

print(group_anagram(strings))
