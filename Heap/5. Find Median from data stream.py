# Time: O(log n), Space: O(1)

# i/p: [5,15,1,3]
# o/p: 5 10 5 4

import heapq
 
class MedianFind:

    def __init__(self):
        self.large = []            #min heap
        self.small = []            #Max heap (store -ve value)
    
    def addNum(self, num):
        # directly push into any one of the heap, lets say small heap
        heapq.heappush(self.small, -1*num)

        # check for balance, small should contain ele < ele of large
        if self.small and self.large and (-1 * self.small[0] >= self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        # check condition for length (diff should not be greater then 1)
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # conditon to check weather large heap's length is not greater than small
        if len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self):
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        return (-1*self.small[0] + self.large[0]) / 2
    









    # Initialize the object
finder = MedianFind()

# Test Case 1: First number
finder.addNum(5)
print(f"Added 5, Median: {finder.findMedian()}") # Expected: 5

# Test Case 2: Even number of elements
finder.addNum(15)
print(f"Added 15, Median: {finder.findMedian()}") # Expected: (5+15)/2 = 10.0

# Test Case 3: Odd number of elements
finder.addNum(1)
print(f"Added 1, Median: {finder.findMedian()}") # Expected: 5

# Test Case 4: Even number again
finder.addNum(3)
print(f"Added 3, Median: {finder.findMedian()}") # Expected: (3+5)/2 = 4.0