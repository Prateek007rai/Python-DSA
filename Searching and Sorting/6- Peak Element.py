# Peak Element
# i/p -> [1,2,3,1]
# o/p -> 2 (ndex)

def peak_element(arr):
    l, r = 0, len(arr) - 1
    
    # Use l < r so that mid + 1 is always a valid index
    while l < r:
        mid = (l + r) // 2
        
        # Check if we are on an upward slope
        if arr[mid] < arr[mid + 1]:
            # Peak must be to the right (and is NOT mid)
            l = mid + 1
        else:
            # We are on a downward slope; peak is to the left (or IS mid)
            r = mid
            
    # When the loop ends, l == r, pointing to a peak
    return l

print(peak_element([1, 2, 3, 1])) # Output: 2