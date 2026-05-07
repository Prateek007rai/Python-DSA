

def subarray_sum(arr, k):
    count = 0                                       # Total subarrays found
    prefix = 0                                      # Running total (Prefix Sum)
    mp = {0: 1}                                     # History: {Sum : Frequency} | 0:1 handles sum starts from index 0

    for num in arr:
        prefix = prefix + num                       # Update running sum

                                                    # If (current - k) exists in history, we found k-sum gap
        if (prefix - k) in mp:
            count = count + mp[(prefix - k)]        # Add frequency of that past sum
        
                                                    # Record this prefix sum in history for future matches
        mp[prefix] = mp.get(prefix, 0) + 1
        
    return count

print(subarray_sum([1,1,1], 2))                     # Output: 2
