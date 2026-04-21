# Time: O(n), Space: O(n)
# i/p: [2,1,5,6,2,3]
# o/p: 10

def largest_area(heights):
    stack = []
    max_area = 0

    for i in range(len(heights)+1):
        if i == len(heights):
            h = 0
        else:
            h = heights[i]
        
        while stack and h < heights[stack[-1]]:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        
        stack.append(i)
    return max_area

print(largest_area([2,1,5,6,2,3]))