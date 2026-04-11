# Also known as 'Split Array Largest Sum'
# i/p: [12, 34, 67, 90], m = 3 (students)
# o/p: 113


def allocate_min(arr, students):
    l, r = max(arr), sum(arr)                     # Range: [Max element, Total sum]

    def is_valid(limit):
        student = 1                               # Start with first student
        newPages = 0                              # Reset current student's pages

        for num in arr:
            if num + newPages <= limit:           # Check if book fits current limit
                newPages = newPages + num         # Assign book to current student
            else:
                newPages = num                    # Move to next student
                student += 1                      # Increment student count
        return student < students                 # Valid if students used < m

    while l < r:
        mid = (l + r) // 2                        # Test the middle of the range

        if is_valid(mid):                         # If valid, try a smaller limit
            r = mid                               # Shrink range to the left
        else:
            l = mid + 1                           # If invalid, increase the limit
            
    return l                                      # Final minimum maximum pages

# --- DRY RUN SUMMARY ---
# 1. mid=113 -> students=2 -> (2 < 3) is True  -> r = 113
# 2. mid=112 -> students=3 -> (3 < 3) is False -> l = 113
# Loop ends, returns 113.

print(allocate_min([12, 34, 67, 90], 3))