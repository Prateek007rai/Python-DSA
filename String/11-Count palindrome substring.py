def count_palindrome_substring(s):
    count = 0
    
    for i in range(len(s)):
        for l, r in [(i,i), (i, i+1)]:
            
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
    return count

print(count_palindrome_substring("aaa")) 