# Find Shortest path from the source to all nodes, but not for -ve weights.
# Time: O(E * log V), Space: O(V)

# i/p: n=4, edges=[(0,1,4), (0,2,1), (2,1,2), (1,3,1), (2,3,5)], src=0
# o/p: [0,3,1,4] <--- these are the wt. of path


import heapq

def dijikstra(n,edges,src):
    graph = {i: [] for i in range(n)}

    for u,v,w in edges:
        graph[u].append((v,w))
        graph[v].append((u,w))

    dist = [float('inf')] * n
    dist[src] = 0 

    heap=[(0,src)]

    while heap:
        distance, node = heapq.heappop(heap)

        if distance > dist[node]:
            continue

        for neighbour, wt in graph[node]:

            if distance + wt < dist[neighbour]:
                dist[neighbour] = distance + wt
                heapq.heappush(heap, (distance + wt, neighbour))

    return dist

