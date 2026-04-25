# Recursive approach
# TIme: O(n), Space: O(n)


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def height_tree(root):
    # Base condition
    if not root:
        return 0
    
    left = height_tree(root.left)
    right = height_tree(root.right)

    return 1 + max(left, right)