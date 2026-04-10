# Given heights of bars, find largest rectangle area
# i/p: [2,1,5,6,2,3]
# o/p: 10


def largest_rectangle(heights):
    stack = []                             # store indices
    max_area = 0
    heights.append(0)                      # extra 0 to empty stack

    for i in range(len(heights)):
        while stack and heights[i] < heights[stack[-1]]:
            h = heights[stack.pop()]       # height of bar

            if stack:
                width = i - stack[-1] - 1  # width between elements
            else:
                width = i                 # full width

            max_area = max(max_area, h * width)   # update max

        stack.append(i)                   # push index

    return max_area

print(largest_rectangle([2,1,5,6,2,3]))