# Time: O(n), Space: O(n)

# i/p: [2,1,2,4,3]
# o/p: [4,2,4,-1,-1]

def next_greater(nums):
    stack = []
    res = [-1]*len(nums)

    for i in range(len(nums) -1, -1, -1):
        while stack and stack[-1] <= nums[i]:
            stack.pop()

        # fill at ith position from stack(top element)
        if stack:
            res[i] = stack[-1]
        stack.append(nums[i])

    return res

print(next_greater([2,1,2,4,3]))