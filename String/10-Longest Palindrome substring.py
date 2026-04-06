# Longest palindrome sub string
# i/p - "babad"
# o/p - "bab"

def longest_palindrome(s):
    res = ""

    for i in range(len(s)):
        # handles both case: for odd (i, i), and for even (i, i+1), ex - "NOON", "RADAR"
        for l,r in [(i, i), (i, i+1)]:
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > len(res):
                    res = s[l:r+1]
                l -= 1                 #move 'l' move more towards left
                r += 1                 #move 'r' move more towards right
    
    return res


print(longest_palindrome("babad"))