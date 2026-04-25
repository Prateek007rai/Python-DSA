# Time: O(n), Space: O(n)
# for tree, suppose : [-10, 9, 20, null, null, 15, 7],      o/p: 42 (15 -> 20 -> 7)

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_path_sum(root):
    max_sum = float('-inf')

    def dfs(node):
        nonlocal max_sum
        if not node:
            return 0
        
        left = max(0, dfs(node.left))
        right = max(0, dfs(node.right))

        # Check if the path through THIS node is the global maximum
        current_path_sum = node.val + left + right
        max_sum = max(max_sum, current_path_sum)

        # Return the best "single-arm" path to the parent
        return node.val + max(left, right)

    dfs(root)
    return max_sum

def build_tree(arr):
    if not arr: return None
    root = TreeNode(arr[0])
    queue = deque([root])
    i = 1
    while queue and i < len(arr):
        curr = queue.popleft()
        if i < len(arr) and arr[i] is not None:
            curr.left = TreeNode(arr[i])
            queue.append(curr.left)
        i += 1
        if i < len(arr) and arr[i] is not None:
            curr.right = TreeNode(arr[i])
            queue.append(curr.right)
        i += 1
    return root

# --- Execution ---
input_arr = [-10, 9, 20, None, None, 15, 7]
root = build_tree(input_arr)
print(f"Max Path Sum: {max_path_sum(root)}")