# Time: O(E), Space: O(V)
# i/p: n=3, edges = [[0,1], [0,2], [1,2]]
# o/p: [2,2,2]

def deg_graph(n, edges):
    deg = [0] * n
    print(deg)

    for u,v in edges:
        deg[u] += 1
        deg[v] += 1
    return deg

print(deg_graph(3, [[0,1], [0,2], [1,2]]))
