# Time: O(n), Space: O(n)

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
