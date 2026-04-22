# Time: O(n),Space: O(n)

# i/p: [1,2,3,4,5], n = 3 
# o/p: [1,2,4,5]

def delete_middle(stack, n):
    if n == 1:
        stack.pop()
        return
    
    temp = stack.pop()
    delete_middle(stack, n-1)
    stack.append(temp)

    return stack

print(delete_middle([1,2,3,4,5], 3))