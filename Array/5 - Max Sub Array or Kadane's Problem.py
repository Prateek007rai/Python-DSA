
def max_subarray(arr):
    curr = arr[0]
    max_sum = arr[0]
    
    for i in range(1, len(arr)):
        curr = max(arr[i], curr+arr[i])
        max_sum = max(max_sum, curr)
    
    return max_sum
    
print(max_subarray([-2, 1, -3,4,-1,2,1]))
            