# Time: O(n), Space: O(h)
# left tree - right tree <= 1

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBalanced(root):
    def dfs(node):
        if not node:
            return 0
        
        left = dfs(node.left)
        if left == -1: return -1
        
        right = dfs(node.right)
        if right == -1: return -1
        
        if abs(left - right) > 1:
            return -1
        
        return 1 + max(left, right)
    
    return dfs(root) != -1

# --- Execution ---
def build_tree(arr):
    if not arr: return None
    root = TreeNode(arr[0])
    q = deque([root])
    i = 1
    while q and i < len(arr):
        curr = q.popleft()
        if i < len(arr) and arr[i] is not None:
            curr.left = TreeNode(arr[i]); q.append(curr.left)
        i += 1
        if i < len(arr) and arr[i] is not None:
            curr.right = TreeNode(arr[i]); q.append(curr.right)
        i += 1
    return root

# Test Case 1: Balanced
t1 = build_tree([3, 9, 20, None, None, 15, 7])
print(f"Balanced Case: {isBalanced(t1)}") # Output: True

# Test Case 2: Unbalanced
t2 = build_tree([1, 2, 2, 3, 3, None, None, 4, 4])
print(f"Unbalanced Case: {isBalanced(t2)}") # Output: False