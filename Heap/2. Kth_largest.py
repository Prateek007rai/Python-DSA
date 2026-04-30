# Time: O(n.log k), Space: O(k)

# i/p: [3,2,1,5,6,4], k = 2
# o/p: 5

import heapq

def kth_largest(arr,k):
    heap = []

    for num in arr:

        heapq.heappush(heap,num)

        if len(heap) > k:
            heapq.heappop(heap)
    
    return heap[0]

