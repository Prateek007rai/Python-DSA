# Time: O(n + pair), Space: O(n)

# i/p: [1,5,7,-1,5], target=6
# o/p: (1,5), (7,-1), (1,5)


def pair_sum(arr, target):
    mp = {}
    res= []

    for i in range(len(arr)):
        diff = target - arr[i]

        if diff in mp:
            for j in range(mp[diff]):
                print(diff, arr[i])
        
        if arr[i] in mp:
            mp[arr[i]] += 1
        else:
            mp[arr[i]] = 1

print(pair_sum([1,5,7,-1,5], 6))
