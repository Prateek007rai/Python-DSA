# Time: O(n), Space: O(n)
# i/p: [1,1,1], K=2
# o/p: 2

def subarray_sum(arr, k):
    count = 0
    prefix = 0            #running sum
    mp = {0: 1}           #base condition for sum = 0

    for num in arr:
        prefix = prefix + num

        if (prefix-k) in mp:
            count = count + mp[(prefix-k)]
        
        mp[prefix] = mp.get(prefix, 0) + 1
    return count

print(subarray_sum([1,1,1], 2))