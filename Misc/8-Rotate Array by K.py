# Rotate the array by K
# input: [1,2,3,4,5,6,7], k = 3
# output: [5,6,7,1,2,3,4]

def rotate_arr(arr, k):
    n = len(arr)

    def reverse(nums, l , r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        return nums
     

    arr = reverse(arr, 0, n-1)
    arr = reverse(arr, 0, k-1)
    arr = reverse(arr, k, n-1)

    return arr


print(rotate_arr([1,2,3,4,5,6,7], 3))