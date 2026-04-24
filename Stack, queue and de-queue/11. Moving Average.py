# Goal: Keep average of the last k numbers.
# Time: O(1) for any size of list, that s why it is better than normal list

# Input: [1, 10, 3, 5], k=3 -> Output: [1.0, 5.5, 4.66, 6.0]

from collections import deque

def moving_avg(nums, k):
    avgs = []
    q = deque()
    curr_sum = 0

    for num in nums:
        if len(q) == k:
            curr_sum = curr_sum - q.popleft()
        
        curr_sum = curr_sum + num
        q.append(num)
        avgs.append(curr_sum/len(q))

    return avgs

print(moving_avg([1, 10, 3, 5], 3))