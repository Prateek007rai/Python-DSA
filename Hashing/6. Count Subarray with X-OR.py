# Time: O(n) | Space: O(n)
# Input: [4,2,2,6,4], k=6 -> Output: 4

def subarray_sum_using_xor(arr, k):
    mp = {0:1}              # History: {XOR_Sum : Frequency} | 0:1 handles XOR sum from index 0
    count = 0
    xr = 0                  # Running XOR

    for num in arr:
        xr = xr ^ num       # Update running XOR sum

        # Logic: If (xr ^ k) exists in history, then the gap must have XOR sum k
        if (xr ^ k) in mp:
            count = count + mp[xr ^ k]
        
        # Store current XOR sum frequency in history
        mp[xr] = mp.get(xr, 0) + 1
    
    return count

print(subarray_sum_using_xor([4,2,2,6,4], 6)) # Output: 4