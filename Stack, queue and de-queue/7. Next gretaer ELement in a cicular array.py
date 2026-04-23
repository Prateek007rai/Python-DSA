# Time: O(n), Space: O(n)
# i/p: [1,2,1]
# o/p: [2,-1,2]

def NGE_circular_array(arr):
    n = len(arr)
    res = [-1] * n
    stack = []
    
    for i in range(2*n -1, -1, -1):
        while stack and stack[-1] <= arr[i % n]:
            stack.pop()
         
        if i<n and stack:
            res [i] = stack[-1]
        
        stack.append(arr[i % n])

    
    return res
    
   
print(NGE_circular_array([1,2,1]))
