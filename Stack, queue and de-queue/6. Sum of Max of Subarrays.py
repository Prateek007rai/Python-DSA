# Time: O(n), Space: O(n)
# i/p: [1,3,2]
# o/p: 15

def sum_subarray(arr):
    n = len(arr)
    l,r,stack = [0]*n, [0]*n, []

    for i in range(n):
        while stack and arr[stack[-1]] < arr[i]:
            stack.pop()
        
        if stack:
            l[i] = i - stack[-1]
        else:
            l[i] = i + 1
        stack.append(i)
    
    stack = []
    for i in range(n):
        while stack and arr[stack[-1]] < arr[i]:
            stack.pop()
        if stack:
            r[i] = i - stack[-1]
        else:
            r[i] = i + 1
        stack.append(i)
    
    return sum(arr[i]*l[i]*r[i] for i in range(n))

    
print(sum_subarray([1,3,2]))