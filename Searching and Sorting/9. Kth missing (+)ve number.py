# Find kth missing number
# i/p: [2,3,4,7,11], k = 5
# 
# Time: O(log n), space : O(1)


def kth_missing(arr, k):
    l,r = 0, len(arr) - 1

    while l <= r:
        mid = (l+r)//2
        missing = arr[mid] - mid + 1

        if missing <= k:
            l = mid + 1
        else:
            r = mid - 1
    return l + k

print(kth_missing([2,3,4,7,11], 5))