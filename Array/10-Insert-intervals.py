# insert intervals
# i/p: Intervals arr = [[1, 3], [6, 9]], new = [2, 5]
# o/p: [[1, 5], [6, 9]]

def insert_intervals(intervals, new):
    intervals.append(new)
    intervals.sort()
    n= len(intervals)
    res = [intervals[0]]

    for i in range(1, n):
        last = res[-1]
        if last[1] > intervals[i][0]:
            last[1] = max(last[1], intervals[i][1])
        else:
            res.append(intervals[i])

    return res

print(insert_intervals([[1, 3], [6, 9]], [2, 5]))                     #[[1, 5], [6, 9]]
