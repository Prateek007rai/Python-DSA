# Smallest Window Containing All Chars:
# i/p: String = "ADOBEDCODEBANC", t= "ABC"
# o/p: "BANC"  

from collections import Counter

def small_window(s, t):
    need = Counter(t)                   # required chars
    have = {}                           # current window

    required = len(need)                # total unique chars
    formed = 0                          # matched chars

    l = 0                               # left pointer
    res = ""                            # result

    for r in range(len(s)):
        ch = s[r]                      # visit char
        have[ch] = have.get(ch, 0) + 1   # check its freq count
        
        if ch in need and have[ch] == need[ch]:       # if freq matched then add
            formed += 1
            
        while required == formed:
            
            if res == "" or len(s[l:r+1]) < len(res):
                res = s[l:r+1]            # update smallest
            
            have[s[l]] -= 1                    # remove left char
            if s[l] in need and have[s[l]] < need[s[l]]:
                formed -= 1
            
            l += 1
    
    return res
    

print(small_window("ADOBEDCODEBANC", "ABC"))