# Find max subarray sum in circular array -------- (All negative → return max element)
# i/p: [5,-3,5]
# o/p: 10


def max_circular_subarray(nums):
    total = 0

    curr_max = curr_min = 0
    max_sum = float('-inf')
    min_sum = float('inf')

    for num in nums:
        curr_max = max(num, curr_max + num)    # normal kadane
        max_sum = max(max_sum, curr_max)

        curr_min = min(num, curr_min + num)    # min subarray
        min_sum = min(min_sum, curr_min)

        total += num

    if max_sum < 0:                            # all negative case
        return max_sum

    return max(max_sum, total - min_sum)       # best of both

print(max_circular_subarray([5,-3,5]))