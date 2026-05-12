# Find shortest path distance from source to all nodes (also deals with -ve values)
# Time: O(V * E), Space: O(V)

def bellman_fords(n, edges, src):
    dist = [float('inf')] * n
    dist[src] = 0

    for _ in range(n-1):
        for u,v,w in edges:
            print("see -> ", dist)
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    for u,v,w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            print("negative cycle detected")
            return None
    
    print(dist)
    return dist

    
print(bellman_fords(5,[(0,1,-1), (0,2,4), (1,2,3), (1,3,2), (1,4,2), (3,2,5), (3,1,1),(4,3,-3)],0))               # o/p: [0,-1,2,-2,1] 
