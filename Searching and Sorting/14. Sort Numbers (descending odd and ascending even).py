# Sort the numbers - Odds in desc folloed by even in asec
# i/p: [1,3,2,4,7,9,8,10]
# o/p: [9,7,3,1,2,4,8,10]

# Time: O(n log n), Space: O(1)

def sort_arr(arr):
    odds = []
    even = []

    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            even.append(arr[i])
        else:
            odds.append(arr[i])
    
    # then sort
    even.sort()
    odds.sort(reverse = True)

    return odds + even

print(sort_arr([1,3,2,4,7,9,8,10]))