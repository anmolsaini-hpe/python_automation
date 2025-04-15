# arr = [1,4,45,6,10,8]
# target = 13
# arr = [1, 2, 4, 3, 6, 7] 
# target = 10
arr = [40, 20, 10, 3, 6, 7]
target = 24

def triplet_sum(arr, target):
    arr.sort()
    #arr = [1, 4, 6, 8, 10, 45]
    for i in range(0, len(arr) - 2):
        left = i + 1
        right = len(arr) - 1

        while left < right:
            sum = arr[i] + arr[left] + arr[right]
            if sum == target:
                return True
            elif sum < target:
                left +=1
            else:
                right -=1
    return False


print(triplet_sum(arr, target))
