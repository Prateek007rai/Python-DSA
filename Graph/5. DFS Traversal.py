# Time: O(E+V), Space: O(V)

# i/p: n=4, edges=[[0,1], [0,2], [1,3]], start=0
# o/p: [0,1,3,2]

# First: convert edges to adj. list
def convert(n, edges):
    graph = {i: [] for i in range(n)}
    
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    return graph

def DFS_traversal(n, start, edges):
    graph = convert(n, edges)

    visited= set([start])
    result= []

    def helper(node):
        result.append(node)
        for i in graph[node]:
            if i not in visited:
                visited.add(i)
                helper(i)
    
    helper(start)
    return result

print(DFS_traversal(4, 0, [[0,1], [0,2], [1,3]]))