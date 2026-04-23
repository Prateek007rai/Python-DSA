# Problem: I only care about how many people entered this door in the last 5 minutes. Anyone who entered more than 5 minutes ago doesn't count anymore.

# Goal: Return pings in the range [t-3000, t].
# Input: [1, 100, 3001, 3002] -> Output: [100, 3001, 3002]

from collections import deque

def count_ping(pings):
    q = deque()

    for i in pings:
        q.append(i)
        while q[0] < (i-3000):    #problem mentioned 5 min = 3000 ms  
            q.popleft()

    return list(q)

print(count_ping([1, 100, 3001, 3002]))

