#  Kth element of 2 sorted arrays
#  i/p: a = [2,3,6,7,9], b = [1,4,8,10], k = 5

def kth_element(a, b, k):
    i = j = 0                                     # Start pointers at 0 for both arrays
    
    while True:
        if i == len(a):                           # If array 'a' is empty
            return b[j + k - 1]                   # The result must be in array 'b'
            
        if j == len(b):                           # If array 'b' is empty
            return a[i + k - 1]                   # The result must be in array 'a'
        
        if k == 1:                                # Base case: looking for the 1st smallest
            return min(a[i], b[j])                 # Smallest of the current two elements
        
        mid = k // 2                              # Split k to jump half the distance
        
        new_i = min(i + mid, len(a)) - 1          # Jump target in 'a' (safety checked)
        new_j = min(j + mid, len(b)) - 1          # Jump target in 'b' (safety checked)
        
        if a[new_i] <= b[new_j]:                  # If jump point in 'a' is smaller
            k -= (new_i - i + 1)                  # Subtract skipped elements from k
            i = new_i + 1                         # Move pointer forward in 'a'
        else:                                     # If jump point in 'b' is smaller
            k -= (new_j - j + 1)                  # Subtract skipped elements from k
            j = new_j + 1                         # Move pointer forward in 'b'

# --- TEST ---
# Combined: [1, 2, 3, 4, 6, 7, 8, 9, 10]
# 5th element is 6
print(kth_element([2, 3, 6, 7, 9], [1, 4, 8, 10], 5))