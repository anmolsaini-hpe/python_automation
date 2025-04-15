N = 4 
M = 4
arr = [1, 4, 5, 7]
brr = [10, 20, 30, 40]
# X = 32
X = 50


def close_pair(arr,brr,N,M,X):
    closest_pair = []
    left = 0
    right = len(brr) - 1
    min_diff = float('inf')

    while left < len(arr) and right >= 0:
        sum = arr[left] + brr[right]
        diff = abs(X - sum)

        if diff < min_diff:
            min_diff = diff
            closest_pair = [arr[left], brr[right]]

        if sum < X :
            left += 1
        else:
            right -= 1
    
    return closest_pair


print(close_pair(arr,brr,N,M,X))