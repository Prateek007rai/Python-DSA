# Time: O(n.log k), Space: O(n)

# i/p: [1,1,1,2,2,3], k = 2
# o/p: [1,2]

import heapq
from collections import Counter

def top_k_freq(arr, k):
    freq = Counter(arr)
    heap = []
    res = []

    # print(freq)
    for num,count in freq.items():
        heapq.heappush(heap, [num,count])

        if len(heap) > k:
            heapq.heappop(heap)
    print(heap)

    for count, num in heap:
        res.append(num)

    return res


print(top_k_freq([1,1,1,2,2,3], 2))
