# Time: O(n), Space: O(n)
# Idea: Do Swap -> the recurse


def flip_tree(root):

    if not root:
        return None
    
    root.left, root.right  =  root.right, root.left

    flip_tree(root.left)
    flip_tree(root.right)

    return root