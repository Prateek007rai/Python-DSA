# Time: O(n*m), Space: O(h)
# i/p: root, subroot
# o/p: boolean

def is_same(a,b):
    if not a and not b:
        return True
    
    if not a or not b:
        return False
    
    return (a.val == b.val and is_same(a.left, b.left) and is_same(a.right, b.right))
    

def is_subtree(root, subroot):
    if not root:
        return False
    
    if is_same(root, subroot):
        return True
    
    return (is_subtree(root.left, subroot) or
            is_subtree(root.right, subroot))
