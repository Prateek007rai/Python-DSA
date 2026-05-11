# insert intervals
# i/p: Intervals arr = [[1, 3], [6, 9]], new = [2, 5]
# o/p: [[1, 5], [6, 9]]

def insert_intervals(intervals, new):
    intervals.append(new)
    intervals.sort()
    n= len(intervals)
    res = [intervals[0]]

                   #[[1, 5], [6, 9]]
