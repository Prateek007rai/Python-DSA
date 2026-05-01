# Time: O(n. log n), Space: O(n)

# i/p: [4,3,2,6]
# o/p: 29

import heapq

def min_cost(arr):
    heapq.heapify(arr)
    cost = 0
    total = 0
    while len(arr) > 1:
        first= heapq.heappop(arr)
        second= heapq.heappop(arr)

        total = first + second
        cost  = total + cost

        heapq.heappush(arr, total)
    
    return cost

print(min_cost([4,3,2,6]))