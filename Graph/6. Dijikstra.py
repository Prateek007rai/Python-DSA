# Find Shortest path from the source to all nodes, but not for -ve weights.
# Time: O(E * log V), Space: O(V)

# i/p: n=4, edges=[(0,1,4), (0,2,1), (2,1,2), (1,3,1), (2,3,5)], src=0
# o/p: [0,3,1,4] <--- these are the wt. of path