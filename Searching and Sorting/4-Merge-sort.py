# merge sort
# i/p - [38, 27, 43, 3, 9, 82, 10]
# o/p - [3, 9, 10, 27, 38, 43, 82]

def merge_sort(arr):
    # if arr size is less than 1 then return
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_side = arr[:mid]
    right_side = arr[mid:]
    
    left_sorted = merge_sort(left_side)
    right_sorted = merge_sort(right_side)
    
    return merge(left_sorted, right_sorted)

def merge(arr1, arr2):
    res = []
    i=0
    j=0
    
    while i<len(arr1) and j<len(arr2):
        if arr1[i] < arr2[j]:
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1
    
    while i < len(arr1):
        res.append(arr1[i])
        i += 1
        
    while j < len(arr2):
        res.append(arr2[j])
        j += 1
        
    return res
    
arr = [38, 27, 43, 3, 9, 82, 10]
print(merge_sort(arr))
    