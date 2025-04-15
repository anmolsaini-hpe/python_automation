# nums = [2, 3, -2, -4, 5, 2, 8, 11]
k = 3
nums = [3, 2, 4, -4, -5, -6, -8, 12]
k = 4
output = []

def sliding_window_maximum(nums, k):
    for i in range(0, len(nums) - k + 1):
        max_window = max(nums[i:k])
        output.append(max_window)
        # print(output)
        k += 1
    return output


print(sliding_window_maximum(nums, k))
