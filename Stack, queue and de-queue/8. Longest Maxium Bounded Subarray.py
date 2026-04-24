# Time: O(n), Space: O(n)

# i/p: [8,2,4,7], limit = 4
# o/p: 2


from collections import deque

def long_bounded(arr, limit):
    max_dq = deque()
    min_dq = deque()
    left = max_len = 0

    print(f"Starting with Array: {arr}, Limit: {limit}\n")

    for right in range(len(arr)):
        val = arr[right]
        
        # Maintain Max Deque (Monotonic Decreasing)
        while max_dq and arr[max_dq[-1]] <= val:
            max_dq.pop()
        max_dq.append(right)

        # Maintain Min Deque (Monotonic Increasing)
        while min_dq and arr[min_dq[-1]] >= val:
            min_dq.pop()
        min_dq.append(right)

        # Check if window violates the limit
        while arr[max_dq[0]] - arr[min_dq[0]] > limit:
            print(f"  ![VIOLATION] at right index {right} (val {val}): Diff {arr[max_dq[0]] - arr[min_dq[0]]} > {limit}")
            left += 1
            if max_dq[0] < left:
                max_dq.popleft()
            if min_dq[0] < left:
                min_dq.popleft()

        # Update max_len
        current_window_len = right - left + 1
        max_len = max(max_len, current_window_len)
        
        print(f"Right Index {right} (Val {val}):")
        print(f"  Window indices: [{left}...{right}] | Current Max: {arr[max_dq[0]]} | Current Min: {arr[min_dq[0]]}")
        print(f"  Max_DQ: {[arr[i] for i in max_dq]} | Min_DQ: {[arr[i] for i in min_dq]} | Length: {current_window_len}")
        print("-" * 50)

    return max_len

print(f"\nFINAL RESULT: {long_bounded([8, 2, 4, 7], 4)}")