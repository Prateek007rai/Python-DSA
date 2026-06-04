# Area contain most water 

def trapping_rain_water(arr):
    l = 0
    r= len(arr) -1
    left_max = 0
    right_max = 0
    sum_water = 0

    while l<r:
        if arr[l] <= arr[r]:
            if arr[l] >  left_max:
                left_max = arr[l]
            else:
                sum_water = sum_water + left_max - arr[l]   
            l += 1     
        else:
            if arr[r] >  right_max:
                right_max = arr[r]
            else:
                sum_water = sum_water + right_max - arr[r]
            r -= 1
    
    return sum_water
    

print(trapping_rain_water([0,1,0,2,1]))
