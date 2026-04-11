# Sort 0s, 1s, 2s
# i/p: [2,0,2,0,1,1,0]
# o/p: [0,0,0,1,1,2,2]


# time: O(n), Space: O(1) - Dutch National Flag Algo







# time: O(n) - Space: O(1)     

def sort_nums(arr):
    count_0 = arr.count(0)
    count_1 = arr.count(1)
    count_2 = arr.count(2)

    res = [0] * count_0 + [1] * count_1 + [2] * count_2 

    return res

print("Way 2 for sorting: ", sort_nums([2,0,2,0,1,1,0])) 