
def product_arr_except_self(arr):
    res = [1] * len(arr)
    prefix = 1
    postfix = 1

    for i in range(len(arr)):
        res[i] = prefix
        prefix = prefix * arr[i]
    
    for i in range(len(arr) - 1, -1, -1):
        res[i] = res[i]*postfix
        postfix = postfix*arr[i]
    return res
    
print(product_arr_except_self([1,2,3,4]))
            
