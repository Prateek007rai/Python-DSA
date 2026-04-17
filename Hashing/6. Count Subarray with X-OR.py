# Time: O(n), Space: O(n)
# i/p: [4,2,2,6,4], k=6
# o/p: 4


def subarray_sum_using_xor(arr, k):
    mp = {0:1}
    count = 0
    xr = 0                  #running X-OR

    for num in arr:
        xr = xr ^ num
        if (xr ^ k) in mp:
            count = count + mp[xr ^ k]
        
        mp[xr] = mp.get(xr, 0) + 1
    
    return count

print(subarray_sum_using_xor([4,2,2,6,4], 6))