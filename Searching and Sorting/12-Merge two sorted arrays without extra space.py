# Merge two sorted arrays without extra space
# Time Complexity: O((n+m)log(n+m))

# i/p: m=[1,5,9,10,15], n=[2,3,8,13]
# o/p: m=[1,2,3,5,8], n=[9,10,13,15]


def merge_arrays(arr1, arr2):
    l,r = len(arr1)-1, 0

    while l >= 0 and r < len(arr2):
        print(arr1[l], arr2[r])
        if arr1[l] > arr2[r]:
            arr1[l], arr2[r] = arr2[r], arr1[l]
        r += 1
        l -= 1   
    
    arr1.sort()
    arr2.sort()

    return arr1, arr2
            

print(merge_arrays([1,5,9,10,15], [2,3,8,13]))