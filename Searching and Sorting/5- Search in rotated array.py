# Search in rotated array
# i/p -> [4,5,6,7,0,1,2], target=0
# o/p -> 4 (index)

def search_rotated_array(arr, target):
    l, r = 0, len(arr)-1
    
    while l <= r:
        mid = (l+r)//2
        if arr[mid] == target:
            return mid
        
        if arr[l] < arr[mid]:
            if arr[l] <= target <arr[mid]:
                r = mid-1
            else: 
                l = mid
        else:
            if arr[mid] <= target <= arr[r]:
                l = mid + 1
            else: 
                r = mid
    
    return -1
    
print(search_rotated_array([4,5,6,7,0,1,2], 0))
    