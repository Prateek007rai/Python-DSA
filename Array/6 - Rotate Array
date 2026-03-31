# ROtate Array
# input: [1,2,3,4,5],  k = 2
# Step 1: [5, 1, 2, 3, 4] (5 moves to the front)
# Step 2: [4, 5, 1, 2, 3] (4 moves to the front)
# output: [4,5,1,2,3]

def rotate_arr(arr, k):
    n = len(arr)
    k = k%n         #suupose if k is 7 or 2 or 12 = move 2 times
    
    def reverse(start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            end -= 1
            start +=1
    
    reverse(0, n-1)
    reverse(0,k-1)
    reverse(k, n-1)
    
    return arr
    
print(rotate_arr([1,2,3,4,5], 2))      #False



# Step	Operation	Array State	Explanation
# Initial	—	[1, 2, 3, 4, 5]	
# Step 1	reverse(0, 4)	[5, 4, 3, 2, 1]	
# Step 2	reverse(0, 1)	[4, 5, 3, 2, 1]	
# Step 3	reverse(2, 4)	[4, 5, 1, 2, 3]	
# Final Output: [4, 5, 1, 2, 3]






    

