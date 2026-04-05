# Longest Repeating char replacment
# i/p - "AABABBA", k = 1
# o/p - 4

def charReplacement(s,k):
    count = {}
    left = 0
    max_freq = 0
    max_window_size = 0
        
    for r in range(len(s)):
        count[s[r]] = count.get(s[r], 0) + 1
        max_freq = max(max_freq, count[s[r]])

        # char needs to be changed = (window_size - max freq) > k
        while (r - left + 1) - max_freq > k :
            count[s[left]] -= 1
            left += 1
        
        # find max window size
        max_window_size = max(max_window_size, r-left+1)
    
    return max_window_size
    
print(charReplacement("AABABBA", 1))