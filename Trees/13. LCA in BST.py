# Time: O(h), Space: O(1)
# Tip: If 
# both > root -> move right
# both < root -> move left
# else: return root
 

def lca_bst(root, p, q):
    while root:
        if p.val < root.val and q.val < root.val:
            root = root.left
        elif p.val > root.val and q.val > root.val:
            root = root.right
        else:
            return root