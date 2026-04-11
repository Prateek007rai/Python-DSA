# Sort 0s, 1s, 2s
# i/p: [2,0,2,0,1,1,0]
# o/p: [0,0,0,1,1,2,2]


# time: O(n), Space: O(1) - Dutch National Flag Algo

def sort_colors(arr):
    l = mid = 0
    r = len(arr) - 1

    while mid <= r:

        if arr[mid] == 0:
            arr[mid], arr[l] = arr[l], arr[mid]
            l += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[r] = arr[r], arr[mid]
            r -= 1

    return arr

print("Way 1 'Dutch National Flag' : ",sort_colors([2,0,2,0,1,1,0]))



# time: O(n) - Space: O(1)     

def sort_nums(arr):
    count_0 = arr.count(0)
    count_1 = arr.count(1)
    count_2 = arr.count(2)

    res = [0] * count_0 + [1] * count_1 + [2] * count_2 

    return res

print("Way 2 for sorting : ", sort_nums([2,0,2,0,1,1,0])) 