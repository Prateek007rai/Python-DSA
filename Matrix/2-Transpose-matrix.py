# transpose the matrix
# i/p - [[1,2], [4,5], [7,8]]
# o/p - [[1, 4, 7], [2, 5, 8]]

def transpose(arr):
    rows = len(arr)
    cols = len(arr[0])
    res = []

    for i in range(cols):
        temp = []
        for j in range(rows):
            temp.append(arr[j][i])
        res.append(temp)
        
    return res
    
print(transpose([[1,2], [4,5], [7,8]]))