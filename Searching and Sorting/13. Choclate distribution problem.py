# Choclate Distribution Problem
# i/p: [7,3,2,4,9,12,56], m = 3
# o/p: 2

def choclate_dist(arr, m):
    if m == 0 or len(arr) == 0:
       return 0
    arr.sort()
    res = float('inf')

    for i in range(len(arr)-m+1):
        diff = arr[i+m-1] - arr[i]
        res = min(diff, res)
   
    return res

print(choclate_dist([7,3,2,4,9,12,56], 3))