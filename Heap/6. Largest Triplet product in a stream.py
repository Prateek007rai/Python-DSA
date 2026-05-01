# Time: O(n. kog 3) ~ O(n), Space: O(3)
# 
# i/p: [1,2,3,4,5]  
# o/p: [-1,-1,6,24,60]

import heapq

def larg_trip_prod(arr):
    res = []
    heap = []

    for num in arr:
        heapq.heappush(heap, num)

        if len(heap) > 3:
            heapq.heappop(heap)
        
        if len(heap) < 3:
            res.append(-1)
        else:
            product = 1
            for i in heap:
                product *= i
            res.append(product)
        
    return res

print(larg_trip_prod([1,2,3,4,5]))