# Time: O(n), space: O(n)
# i/p: 1 is root with 2 and 3, 4 and 5 are 2's children
# o/p: [[1], [2,3], [4,5]]

from collections import deque

def level_order(root):
    res = []
    queue = deque([root])
    
    if not root:
        return []
    
    while queue:
        size = len(queue)
        level = []

        for _ in range(size):
            ele = queue.popleft()
            level.append(ele.val)
            
            if ele.left :
               queue.append(ele.left)
            if ele.right:
                queue.append(ele.right)

            res.append(level)
    
    return res
