
def pair_sum(arr, target):
    seen = set()
    for i in arr:
        x = target - i
        if x in seen:
            return [x, i]
        seen.add(i)
    return 0
    
print(pair_sum([2,6,8,7], 10))
            