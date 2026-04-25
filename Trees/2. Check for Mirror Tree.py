# Time: O(n), Space: O(n)

from collections import deque
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# ------------------------------------ Main ---------------------------------------

def is_Mirror(t1, t2):
    #   if both trees are null
    if not t1 and not t2:
        return True
    
    # if one of three is not empty
    if not t1 or not t2:
        return False
    
    return (
        t1.val == t2.val and
        is_Mirror(t1.left, t2.right) and
        is_Mirror(t1.right, t2.left)
    )

# ---------------------------------- Main Ends ------------------------------------


#  Helper function for tree - No need to do root.left = TreeNode(10), just pass an array in this function, it will make tree
def build_tree(arr):
    root = TreeNode(arr[0])
    queue = deque([root])
    i = 1

    while queue and i < len(arr):
        curr = queue.popleft()

        if i < len(arr) and queue:
            curr.left = arr[i]
            queue.append(curr.left)
        i += 1

        if i < len(arr) and queue:
            curr.right = arr[i]
            queue.append(curr.right)
        i += 1
    
    return root


# --- Execution ---
tree1 = build_tree([1, 2, 3, 4, 5])
tree2 = build_tree([1, 3, 2, None, None, 5, 4])

print(is_Mirror(tree1, tree2)) 

tree3 = build_tree([1, 2, 2, 3, 4, 4, 3])
print(is_Mirror(tree3.left, tree3.right))
