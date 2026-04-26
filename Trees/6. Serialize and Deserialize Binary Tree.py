# Time: O(n), Space: O(n)

# i/p: 1-> 2,3 and 3-> 4,5
# o/p: 1,2,null,null,3,4,null,null,5,null,null

# Serialize, Tree -> String
def serialize(root):
    res = []
    
    def dfs(node):
        if not node:
            res.append("null")
            return 
        res.append(str(node.val))

        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return ",".join(res)    

# De-serialize, String -> Tree
def deserialize(data):
    strData = data.split(",")
    i = 0
    
    def dfs():
        nonlocal i
        if strData[i] == "null":
            i += 1
            return None
        node = TreeNode(int(strData[i]))
        i += 1

        node.left = dfs()
        node.right = dfs()

        return node

    return dfs()
    
