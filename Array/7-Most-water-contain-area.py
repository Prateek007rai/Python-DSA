
# Area contain most water 

def most_water_area_contains(arr):
    l = 0
    r = len(arr) -1
    max_area = 0

    while l < r:
        height = 0
        width = r-l

        # keep the height of min side so that water will not spill
        if arr[l] <= arr[r]:
            height = arr[l]
            l += 1
        else: 
            height = arr[r]
            r -= 1

        area = height * width
        max_area = max(area, max_area)

    return max_area
 
print(most_water_area_contains([1,8,6,2,5,4,8,3,7]))         # output: 49
            