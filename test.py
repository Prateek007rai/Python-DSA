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
    
# Valid paranthesis
def is_valid(s: str) -> bool:
    
# Test Cases
print("Vaild Parantesis: ", is_valid("()[]{}")) # True
print("Vaild Parantesis: ", is_valid("([)]"))   # False
print("Vaild Parantesis: ", is_valid("{[]}"))   # True