# Time: O(n), Space: (1)

# i/p: [10,5,6,2]
# o/p: True

def is_max_heap(arr):
    n = len(arr)

    for i in range(len(arr)):

        left = 2*i+1
        right = 2*i+2

        if left < n and arr[i] < arr[left]:
            return False
        
        if right < n and arr[i] < arr[right]:
            return False
        
    return True

print(is_max_heap([10,5,6,2]))