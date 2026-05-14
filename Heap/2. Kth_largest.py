# Time: O(n.log k), Space: O(k)


import heapq

def kth_largest(arr,k):
    heap = []

    for num in arr:

        heapq.heappush(heap,num)

        if len(heap) > k:
            heapq.heappop(heap)
    
    return heap[0]

print(kth_largest([17, 20, 9, 11, 35, 44, 29], 5))        #17
