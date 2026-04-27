# Time: O(n), space: O(n)
# Construct tree using pre-order and Inorder

def build_tree(preorder, inorder):
    index_map = {v:i for i, v in enumerate(inorder)}
    pre_idx = 0

    def dfs(left, right):
        nonlocal pre_idx
        if left > right:
            return None
        
        root_val = preorder[pre_idx]
        root = TreeNode(root_val)
        pre_idx += 1

        mid = index_map[root_val]
        left = dfs(left, mid -1)
        right = dfs(mid+1, right)

        return root


    return dfs(0, len(inorder) -1)