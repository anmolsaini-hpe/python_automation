# arr = [1, 2, 3, 1, 4, 5, 2, 3, 6]
# k = 3
# arr = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13]
# k = 4
arr = [5, 1, 3, 4, 2, 6]
k = 1
output = []

def max_subarray(arr,k):

    for i in range(0,len(arr) - k +1):
        max_subarray = max(arr[i:k])
        k += 1
        output.append(max_subarray)

    return output

print(max_subarray(arr,k))
