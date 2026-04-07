# first and last occurence of char
# i/p - [1,2,2,2,3], 2
# o/p - [1,3]

def first_last(arr, target):
    
    def first_occ():
        l, r = 0, len(arr)-1
        res = -1

        while l <= r:
            mid = (l+r)//2
            if arr[mid] == target:
                res = mid
                r = mid-1                 #go left
            elif arr[mid] < target:
                l = mid + 1
            else: 
                r = mid-1
        return res
    
    def last_occ():
        l, r = 0, len(arr)-1
        res = -1

        while l <= r:
            mid = (l+r)//2
            if arr[mid] == target:
                res = mid
                l = mid+1                 #go right
            elif arr[mid] < target:
                l = mid + 1
            else: 
                r = mid-1
        return res
                
    
    first = first_occ()
    last = last_occ()
   
    return [first, last]

print(first_last([1,2,2,2,3], 2))