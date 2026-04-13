# Time: O(n), Space: O(n)
# i/p: [100,4,200,1,3,2]
# o/p: 4

def largest_sequence(arr):
    s = set()
    longest = 0

    for num in arr:
        s.add(num)

    for num in s:
        if num-1 not in s:
            count = 1
            curr = num
            while curr + 1 in s:
                count += 1
                curr += 1
            if count > longest:
                longest = count

    return longest


print(largest_sequence([100,4,200,1,3,2]))