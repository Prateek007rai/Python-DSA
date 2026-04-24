# Time: O(n), Space: O(k)

# i/p: [1,3,-1,-3,5], k=3
# o/p: [3,3,5]

from collections import deque

def max_sliding_window(nums, k):
    res = []
    dq = deque()

    for i in range(len(nums)):
        # maintain the deque size
        while dq and dq[0] <= i-k:
            dq.popleft()

        # pop if value is smaller
        while dq and nums[dq[0]] <= nums[i]:
            dq.pop()

        # insert into the res
        dq.append(i)
        if i >= k-1:
            res.append(nums[dq[0]])

    return res

print(max_sliding_window([1,3,-1,-3,5], 3))