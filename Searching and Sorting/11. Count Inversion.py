# Count pairs (i,j) such that i < j and arr[i] > arr[j]
# i/p: [2,4,1,3,5]
# o/p: 3       .... 3 values are (2,1),(4,1),(4,3)


def count_inversions(arr):
 
    def merge_sort(nums):
        if len(nums) <= 1:
            return nums, 0
        
        mid = len(nums) // 2

        left, inv1 = merge_sort(nums[:mid])
        right, inv2 = merge_sort(nums[mid:])

        merged_both, inv3 = merging(left, right)
    
        return merged_both, (inv1 + inv2 + inv3)

    def merging(left, right):
        i = j = inv = 0
        res = []

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                inv = inv + len(left)- i
                j += 1
        
        # fill remaining
        res.extend(left[i:])
        res.extend(right[j:])
            
        return res, inv


    return merge_sort(arr)


print(count_inversions([2,4,1,3,5]))