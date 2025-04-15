numbers = [2,7,11,15]
target = 9
# numbers = [3,2,4]
# target = 6


def two_sum(numbers, target):
    ht = {}
    for i in range(len(numbers)):
        num1 = numbers[i]
        required_num = target - num1
        if required_num in ht:
            return [ht[required_num], i]
        else:
            ht[num1] = i
    return []

print(two_sum(numbers, target))