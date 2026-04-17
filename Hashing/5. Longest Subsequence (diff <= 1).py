# Time: O(n), Space: O(n)
# i/p: [1,2,2,3,1,2]
# o/p: 5

def longest_sub(arr):
    mp = {}
    max_len = 0

    # update counter in arr loop
    for num in arr:
        mp[num] = mp.get(num, 0) + 1

    # loop in mp(hashing)
    for num in mp:
        curr = mp[num]
        if (num+1) in mp:
            curr = curr + mp[num+1]
        
        max_len = max(curr, max_len)
    
    return max_len
    

print(longest_sub([1,2,2,3,1,2]))