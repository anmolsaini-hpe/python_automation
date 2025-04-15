arr = [1,2,3,4,5]

# arr = [3, 4, 5]

def triplet(arr):
    for i in range(0,len(arr)):
        left = 0
        right = len(arr) - 1 
        
        while left < right :
            sum = arr[left] + arr[right]
            if sum == arr[i]:
                return True
            elif sum < arr[i]:
                left += 1
            else:
                right -= 1
    return False

print(triplet(arr))