# Practice
# 2nd highest number in array 

def find_num(arr):
    first = second = float('-inf')

    for num in arr:
        if num > first: 
            second = first
            first = num
        elif first > num > second:
            second = num
    return second
print(find_num([34,45,53,21,24,64,54]))


# String compression

def compress(str1):
    res = ''
    count = 1

    for i in range(1, len(str1)):
        if str1[i] == str1[i-1]:
            count += 1
        else:
            res = res + str1[i-1] + str(count)
            count = 1
    
    res = res + str1[-1] + str(count) 
    return res

print(compress("aaaaaa"))


# reverse a string
def rev_str(s):
    return s[::-1]

def rev_string(s):
    res = ""

    for ch in s:
       res = ch + res

    return res

print("Reverse a string -> ", rev_string("Prateek"))


# spiral matrix
def spiral(arr):
    top, bottom = 0, len(arr) - 1
    left, right = 0, len(arr[0]) - 1
    res = []

    while top <= bottom and left <= right:
        # print top row
        for i in range(left, right+1):
            res.append(arr[top][i])
        top += 1

        # print right col
        for i in range(top, bottom + 1):
            res.append(arr[i][right])
        right -= 1

        # print bottom row
        for i in range(right, left - 1, -1):
            res.append(arr[bottom][i])
        bottom -= 1

        # print left col
        for i in range(bottom, top-1, -1):
            res.append(arr[i][left])
        left += 1
          
    return res


print(spiral([[1,2,3], [4,5,6], [7,8,9]]))


# transpose matrix
def transpose(arr):
    rows = len(arr)
    cols = len(arr[0])
    res = []

    for i in range(cols):
        temp = []
        for j in range(rows):
            temp.append(arr[j][i])
        res.append(temp)
    
    return res
    
print("Transpose of matrix: ", transpose([[1,2], [3,4], [5,6]]))


# Longest substring without repeating char
def long_sub(s):
    max_len = 0
    seen = set()
    l = 0

    for r in range(len(s)):

        # shrink the sliding window
        while s[r] in seen:
            seen.remove(s[l])
            l += 1

        seen.add(s[r])

        max_len = max(r-l+1, max_len)            #max len or sliding window size(r-l+1)
    
    return max_len

print("Longest substring without repeating char: ", long_sub("abcabcbb"))

# ------------------------------------------------------------------------------------------->
# Count word freeq in a sentence
def count_word_frequency(sentence):
    # Convert to lowercase and split by whitespace
    words = sentence.lower().split()
    
    frequency = {}
    for word in words:
        # If word exists, increment; otherwise, set to 1
        frequency[word] = frequency.get(word, 0) + 1
        
    return frequency

text = "The quick brown fox jumps over the lazy dog the fox"
print(count_word_frequency(text))


# Implement queue using stacks
class MyQueue:
    def __init__(self):
        # s1 acts as the "Input Stack" for new elements
        # s2 acts as the "Output Stack" for extracting elements in FIFO order
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        """Push element x to the back of queue."""
        self.s1.append(x)

    def pop(self) -> int:
        """Removes the element from in front of queue and returns that element."""
        # Ensure s2 is populated by calling peek()
        self.peek() 
        return self.s2.pop()

    def peek(self) -> int:
        """Get the front element."""
        # Only transfer elements if the output stack (s2) is empty
        if not self.s2:
            # Transfer all elements from s1 to s2
            # This effectively reverses the order (LIFO -> FIFO)
            while self.s1:
                self.s2.append(self.s1.pop())
        
        # Return the top of the output stack
        return self.s2[-1]

    def empty(self) -> bool:
        """Returns whether the queue is empty."""
        # The queue is empty only if both stacks have no elements
        return not self.s1 and not self.s2
    
    
# word search
def word_search_in_matrix(arr, word):
    rows = len(arr)
    cols = len(arr[0])

    # dfs for traversing the matrix
    def dfs(r, c, i):
        if i == len(word):
            return True
        if r < 0 or c < 0 or r >= rows or c >= cols:
            return False
        if arr[r][c] != word[i]:
            return False
        
        # now it will match (consider)
        temp = arr[r][c]
        arr[r][c] = '#'               #mark as visited

        found = (
            dfs(r+1, c, i+1) or
            dfs(r-1, c, i+1) or
            dfs(r, c+1, i+1) or
            dfs(r, c-1, i+1)
        )

        arr[r][c] = temp

        return found
    # dfs dunction ends here

    for i in range(rows):
        for j in range(cols):
            if dfs(i,j,0):
                return True
    
    return False


print("Word search in arrray", word_search_in_matrix([['A','B','C'], ['D','E','F'], ['G','H','I']],"ABCFEDGHI"))


# return first non repetitive char from string
def first_non_rep_char(sent):
    counter = {}
    
    for ch in sent.lower():
        counter[ch] = counter.get(ch, 0) + 1
    
    for i in counter:
        if counter[i] == 1:
            return i
    
    return "No unique char is present"

print("First non repetitive char: ", first_non_rep_char("Kasjkasbj"))


# find elements that appears more than n/2 times:
def ele_more_than_nBytwo(arr):
    element = None
    count = 0

    for num in arr:
        if count == 0:
            element = num
        
        if element == num:
            count += 1
        else:
            count -= 1

    return element

print("ELemnet appears more than n/2 times: ", ele_more_than_nBytwo([3,2,3]))


# Longest common prefix
def longest_common_prefix(arr):
    prefix = arr[0]

    for word in arr:
        while word.find(prefix) != 0:
            prefix = prefix[:-1]

    return prefix

print("Longest common prefix: ", longest_common_prefix(['flower', 'flow', 'flown', 'floor', 'fast']))


# Valid paranthesis
def is_valid_paranthesis(s):
    stack = []
    mp = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for ch in s:
        if ch in mp:
            if not stack or stack[-1] != mp[ch]:
                return False
            stack.pop()
        else:
            stack.append(ch)
    return len(stack) == 0

print("Check is valid paranthesis: ", is_valid_paranthesis("()[]{}"))
print("Check is valid paranthesis: ", is_valid_paranthesis("()(()"))


# Longest char repeating replacement
def long_ch_repeat_replace(s, k):
    l = 0
    res = 0
    max_freq = 0
    count = {}

    for r in range(len(s)):
        count[s[r]] = count.get(s[r], 0) + 1
        max_freq = max(max_freq, count[s[r]])

        while (r-l+1) - max_freq > k:
            count[s[l]] -= 1
            l += 1
        
        res = max(res, r-l+1)
    
    return res

print("Check for longest char replacement: ", long_ch_repeat_replace("AABABBB", 1))

# print all anagrams together
def anagrams_together(arr):
    keys = {}

    for word in arr:
        wordVal = "".join(sorted(word))

        if wordVal not in keys:
            keys[wordVal] = []
        keys[wordVal].append(word)
    
    return list(keys.values())

print("Anagram collection: ", anagrams_together(["ate", "eat", "cat", "tac", "sat"]))       



# START A NEW DAY WITH A NEW THOUGHT

# 1. find pair of sum
def pair_sum(arr, target):
    seen = set()

    for num in arr:
        x = target - num
        if x in seen:
            return x, num
        seen.add(num)

    return False

print(pair_sum([4,6,7,8,9], 14))

# 2. Buy and sell stock problem
def buy_sell(arr):
    max_profit = 0
    min_price = arr[0]

    for price in arr:
        min_price = min(price, min_price)

        profit = price - min_price

        max_profit = max(profit, max_profit)
    return max_profit

print(buy_sell([7,1,6,4,3]))

# 3. Move Zeroes to the end
def move_zeroes(arr):
    j=0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    return arr

print(move_zeroes([1,0,0,2,0,3,0,4,5,6,0,0,0,7]))


# 4. Product of arr itself
def product_arr_self(arr):
    res = [1] * len(arr)

    left_product = 1
    for i in range(len(arr)):
        res[i] = left_product
        left_product = left_product * arr[i]
 
    right_product = 1
    for i in range(len(arr)-1, -1, -1):
        res[i] = res[i] * right_product
        right_product = right_product * arr[i]

    return res

print(product_arr_self([1,2,3,4]))

# 5. Maximum subarray problem
def max_subarr(arr):
    curr_sum = arr[0]
    max_sum = arr[0]

    for num in arr[1:]:
        curr_sum = max(curr_sum, curr_sum + num)
        max_sum = max(curr_sum, max_sum)
    
    return max_sum

print(max_subarr([-2,1,-3,4,-1,2,1]))

# 6. Container with most water problem
def max_area(arr):
    left = 0
    max_area = 0
    right = len(arr) - 1

    while left < right:
        width  = right - left

        if arr[left] < arr[right]:
            height  = arr[left]
            left += 1
        else:
            height  = arr[right]
            right -= 1
        max_area = max(max_area, height * width)

    return max_area

print(max_area([1,8,6,2,5,4,6,3,7]))

# 7. Factorial
def factorial(n):
    if n == 1:
        return 1
    
    return n * factorial(n-1)

print(factorial(5))

# 8. Trapping rain water
def trap_water(arr):
    if not arr:
        return 0
        
    left = 0
    right = len(arr) - 1
    
    left_max = arr[left]
    right_max = arr[right]
    
    water_count = 0

    while left < right:
        if arr[left] <= arr[right]:
            # If current height is greater than max left wall, update it
            if arr[left] >= left_max:
                left_max = arr[left]
            else:
                # Otherwise, water is trapped securely by the higher right wall
                water_count += left_max - arr[left]
            left += 1
        else:
            # If right wall is smaller, track from the right side
            if arr[right] >= right_max:
                right_max = arr[right]
            else:
                water_count += right_max - arr[right]
            right -= 1
            
    return water_count

print(trap_water([0, 1, 0, 2, 1]))  # Output: 1
print(trap_water([4, 2, 0, 3, 2, 5]))  # Output: 9


# 9. Merge intervals
def merge_intervals(arr):
    arr.sort()
    res = [arr[0]]
    
    for i in range(1, len(arr)):
        top_ele = res[-1]
        if top_ele[1] < arr[i][0]:
            res.append(arr[i])
        else:
            top_ele[1] = max(arr[i][1], top_ele[1])
    return res

print(merge_intervals([[1,3], [2,6]]))

# 10. Insert merge intervals
def insert_intervals(arr, new):
    arr.append(new)
    arr.sort()
    res = [arr[0]]

    for i in range(1, len(arr)):
        last  = res[-1]

        if last[1] < arr[i][0]:
            res.append(arr[i])
        else:
            last[1] = max(last[1], arr[i][1])
    return res

print(insert_intervals([[1,3],[6,9]], [2,5]))

# 11. Spiral matrix
def spiral_matrix(arr):
    res = []
    top, left = 0, 0
    bottom, right = len(arr)-1, len(arr)-1

    if not arr or len(arr) == 0:
        return None
    
    while top <= bottom and left <= right:

        # insert top elements
        for i in range(left, right+1):
            res.append(arr[top][i])
        top += 1
        
        # insert right side eles
        for i in range(top, bottom+1):
            res.append(arr[i][right])
        right -= 1

        # insert bottom eles
        if top <= bottom:
            for i in range(right, left-1, -1):
                res.append(arr[bottom][i])
            bottom -= 1

        # insert left eles
        if left <= right:
            for i in range(bottom, top-1, -1):
                res.append(arr[i][left])
            left += 1
    
    return res

print(spiral_matrix([[1,2,3], [4,5,6], [7,8,9]]))

# 12. Transpose matrix
def transpose_matrix(arr):
    rows = len(arr)
    res = []

    for i in range(len(arr[0])):
        op_arr = []
        for j in range(rows):
            op_arr.append(arr[j][i])
        res.append(op_arr)
    
    return res

print(transpose_matrix([[1,2], [3,4], [5,6]]))

# 13. Word search
def exist(board, word):
    rows = len(board)
    cols = len(board[0])

    # function for dfs
    def dfs(r, c, i):
        if i == len(word):
            return True
        if r<0 or c<0 or r>rows or c>cols:
            return False
        
        if board[r][c] != word[i]:
            return False
        
        temp = board[r][c]
        board[r][c] = '#'

        found = (
            dfs(r,c+1,i+1) or
            dfs(r-1,c,i+1) or
            dfs(r+1,c,i+1) or
            dfs(r,c-1,i+1)
        )
        board[r][c] = temp
        return found

    for i in range(rows):
        for j in range(cols):
            if dfs(i,j,0):
                return True
    return False

print(exist([['A','B','C'], ['D','E','F'], ['G','H','I']], 'ABE'))


# 14. Palindrome check
def check_pal(s):
    left = 0
    right = len(s)-1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

print(check_pal('madam'))

# 15. Print Fibonacci Series
def print_fib(n):
    a=0
    b=1
    if n==1:
        print(a)
        return
    elif n == 2:
        print(a,b)
        return
    print(a, b, " ")
    for i in range(2, n):
        num = a + b
        a = b
        b = num
        print(num, " ")
    
    return 

print(print_fib(8))

# 24. Print triangle pyramid pattern with numbers
