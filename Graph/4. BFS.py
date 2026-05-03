# Time: O(V+E), Space: O(V)
# i/p: n=4, edges= [[0,1], [0,2], [1,3]], start=0
# o/p: [0,1,2,3]

from collections import deque

# convert to adjacency list
def convert(n, edges):
    graph = {i: [] for i in range(n)}

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    return graph

def BFS_traversal(n, start, edges):
    graph = convert(n, edges)

    visited = set([start])
    queue = deque([start])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for i in graph[node]:
            if i not in visited:
                visited.add(i)
                queue.append(i)
    
    return result
    

print(BFS_traversal(4, 0, [[0,1], [0,2], [1,3]]))