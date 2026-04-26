# Time: O(n), Space: O(h)
# o/p: output is int, ex: 3 (edge, path: 4->2->1->3, edge is 3)

def max_diameter(root):
    max_dia = 0

    def dfs(node):
        nonlocal max_dia

        if not node:
            return 0
        left = dfs(node.left)
        right = dfs(node.right)

        max_dia = max(max_dia, left + right)

        return 1 + max(left, right)

    dfs(root)
    return max_dia