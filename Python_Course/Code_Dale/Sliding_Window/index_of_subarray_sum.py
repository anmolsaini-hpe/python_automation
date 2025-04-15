# arr = [1, 2, 3, 7, 5]
# target = 12
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# target = 15
# arr = [5, 3, 4]
# target = 2
arr = [12, 18, 5, 11, 30, 5]
target = 69

def index_subarray_sum(arr,target):
    curr_sum = 0
    left = 0
    for right in range(0, len(arr)):
        curr_sum += arr[right]
        while curr_sum > target and left <= right :
            curr_sum -= arr[left]
            left +=1
        if curr_sum == target:
            return [left +1 , right +1]
        
    return [-1]
print(index_subarray_sum(arr,target))