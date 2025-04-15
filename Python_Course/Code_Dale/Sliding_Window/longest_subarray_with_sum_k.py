def longest_subarray_with_sum_k(arr, k):
    prefix_sums = {}  # Stores prefix sum and its first occurrence index
    curr_sum = 0
    max_length = 0
    
    for i in range(len(arr)):
        curr_sum += arr[i]

        # Case 1: If the sum itself is k
        if curr_sum == k:
            max_length = i + 1  # Full subarray from 0 to i

        # Case 2: If (curr_sum - k) exists in prefix_sums
        if (curr_sum - k) in prefix_sums:
            max_length = max(max_length, i - prefix_sums[curr_sum - k])
        # Store the first occurrence of curr_sum
        else: 
            prefix_sums[curr_sum] = i

    return max_length

# Example Test
arr = [3, 4, 7]
k = 7
print(longest_subarray_with_sum_k(arr, k))
