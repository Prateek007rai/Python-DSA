# Time: O(E+V), Space: O(V)

# i/p: n=4, edges = [[0,1], [0,2], [1,3]], src = 0, dest = 3
# o/p: True

def convert(n, arr):
    graph  = {}

    for i in range(n):
        graph[i] = []

    for u,v in arr:
        graph[u].append(v)
        graph[v].append(u)
    
    return graph


def has_path(n, edges, src, dest):
    graph = convert(n, edges)
    visited = set()

    def dfs(node):
        if node == dest:
            return True
        visited.add(node)

        for i in graph[node]:
            if i not in visited:
                if dfs(i):
                    return True
        
        return False
    
    return dfs(src)

print(has_path(4, [[0,1], [0,2], [1,3]], 0, 3))