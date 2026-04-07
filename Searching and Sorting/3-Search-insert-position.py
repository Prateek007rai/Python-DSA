# Search insertt positon of target element
# i/p - [1,3,5,6], insert = 2
# o/p - 1 (index)

def search_insert(arr, target):
    l,r = 0, len(arr)-1
    
    while l<=r:
        mid = (l+r)//2
        
        if arr[mid] == target:
           return mid
        elif arr[mid] < target:
            l = mid+1
        else: 
            r = mid-1
    return l

print(search_insert([1,3,5,6],2))