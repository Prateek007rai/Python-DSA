# word search
#use DFS(backtracking)

# spiral matrix traverse

def spiral_traverse(arr):
    if not arr or not arr[0]:
        return []
        
    # define top bottom left right and res
    res = []
    top, bottom = 0, len(arr) - 1
    left, right = 0, len(arr[0]) - 1
    
    # visit and fill the arr, 
    # reduce the size on each visit of side
    while top <= bottom and left <= right:
        # visit top
        for i in range(left, right+1):
            res.append(arr[top][i])
        top += 1
        
        # visit right
        for i in range(top, bottom+1):
            res.append(arr[i][right])
        right -= 1
        
        # visit bottom
        for i in range(right, left -1, -1):
            res.append(arr[bottom][i])
        bottom -= 1
        
        # visit left
        for i in range(bottom, top-1, -1):
            res.append(arr[i][left])
        left += 1
        
        
    return res
            
print(spiral_traverse([[1,2,3], [4,5,6], [7,8,9]]))                   #[1, 2, 3, 6, 9, 8, 7, 4, 5]