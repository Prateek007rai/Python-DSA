# merge intervals
# i/p: intervals arr = [[1, 3], [2, 6], [8, 16], [15, 18]]

def merge_intervals(intervals):
    n = len(intervals)
    intervals.sort()
    res = [intervals[0]]

    for i in range(1, len(intervals)):
        last = res[-1]

        if last[1] > intervals[i][0]:
            last [1] = max(last[1], intervals[i][1])
        else:
            res.append(intervals[i])

    return res
            
print(merge_intervals([[1, 3], [2, 6], [8, 16], [15, 18]]))
