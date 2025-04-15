arr = [100, 200, 300, 400]
# k = 2
# k = 4
k = 1

def max_sum_subarray(arr, k):
    curr_sum = sum(arr[0:k])
    max_sum = curr_sum

    for i in range(k, len(arr)):
        curr_sum = curr_sum + arr[i] - arr[i-k]
        max_sum = max(max_sum, curr_sum)
    
    return max_sum

print(max_sum_subarray(arr, k))
