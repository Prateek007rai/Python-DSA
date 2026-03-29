
def max_profit(arr):
    min_price = arr[0]
    profit = 0
    
    for i in range(len(arr)):
        if arr[i] < min_price:
            min_price = arr[i]
        
        new_profit = arr[i] - min_price
        if(new_profit > profit):
            profit = new_profit
    return profit
    
print(max_profit([9,2,6,1,8,7]))
print(max_profit([7,1,6,4,3]))
            