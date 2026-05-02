# Time: O(E), Space: O(V+E)
# i/p: [[0,1],[0,2],[1,3],[2,3]], n = 4
# o/p: {0 : [1,2], 1: [0,3], 2: [0,3], 3: [1,2]}

def convert(n, arr):
    graph  = {}

    for i in range(n):
        graph[i] = []

    for u,v in arr:
        graph[u].append(v)
        graph[v].append(u)
    
    return graph

print(convert(4, [[0,1],[0,2],[1,3],[2,3]]))