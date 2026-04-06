# Binary search
# Find mid and search again in loop

def binary_search(arr, target):
    l, r = 0, len(arr)-1
    while l <= r:
        mid = (l+r)//2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid+1
        else:
            r=mid-1
    return -1
    
print(binary_search([2,3,4,5,6,7], 6))