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


# Longest substring without repeating char
def long_sub_1(s):
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

print("Longest substring without repeating char: ", long_sub_1("abcabcbb"))

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

# Longest common prefix
def longest_common_prefix1(arr):
    prefix = arr[0]

    for word in arr:
        while word.find(prefix) != 0:
            prefix = prefix[:-1]

    return prefix

print("Longest common prefix: ", longest_common_prefix1(['flower', 'flow', 'flown', 'floor', 'fast']))

# print all anagrams together
def anagrams_together_1(arr):
    keys = {}

    for word in arr:
        wordVal = "".join(sorted(word))

        if wordVal not in keys:
            keys[wordVal] = []
        keys[wordVal].append(word)
    
    return list(keys.values())

print("Anagram collection: ", anagrams_together_1(["ate", "eat", "cat", "tac", "sat"]))  

# Valid paranthesis
def is_valid_paranthesis_1(s):
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

print("Check is valid paranthesis: ", is_valid_paranthesis_1("()[]{}"))

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
    print(a, b, end=" ")
    for i in range(2, n):
        num = a + b
        a = b
        b = num
        print(num, end=" ")
    
    return 

print(print_fib(8))

# 16. Print triangle pyramid pattern with numbers
def print_tri(n):
    num = 1
    for i in range(n):
        print("" * (n-i-1), end= " ")
        for j in range(i+1):
            print(num, end= " ")
            num += 1
        print()
    return None

print(print_tri(3))

# 17. Reverse a number
def rev_num(num):
    res = 0

    while num:
        digit = num % 10
        res = res*10 + digit
        num = num // 10

    return res

print(rev_num(1423))

# 18. Count Vowels in a string
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0

    for ch in s:
       if ch in vowels:
           count += 1
    
    return count

print(count_vowels("Prateek"))

# 19. Check numbers are palindrome
def check_num_isPal(num):
    res = 0
    original = num

    while num > 0:
        digit = num % 10
        res = res * 10 + digit
        num = num // 10
    
    return res == original
print(check_num_isPal(121))

# 20. A - Nth fibnocci number using recursion, time complexity = O(2^n)
def nth_fib(n):

    if n <= 1:
        return n
    
    return nth_fib(n-1) + nth_fib(n-2)

print(nth_fib(10))

# 20. B - iterative approach, time complexity = O(n)
def nth_fib_iter(n):
    if n <= 1:
        return n
    
    a,b = 0, 1

    for _ in range(2, n+1):
        temp  = a + b
        a = b
        b = temp
    
    return b

print(nth_fib_iter(10))

#  21. Way 1 - Valid Anagram
def check_anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    
    for i in range(len(str1)):
        if str1[i] not in str2 or str2[i] not in str1:
            return False
    
    return True
print(check_anagram("listen", "silent"))


# 21. Way 2 - Valid anagram
def check_anagram_counter(str1, str2):
    if len(str1) != len(str2):
        return False
    
    counter = {}
    for ch in str1:
        counter[ch] = counter.get(ch, 0) + 1

    for ch in str2:
        if ch not in counter:
            return False
        counter[ch] = counter[ch] - 1

        if counter[ch] == 0:
            del counter[ch]
    
    return len(counter) == 0

print(check_anagram_counter("listen", "silent"))

# 22. First Non Repeating Char Index
def first_unique_char_index(s):
    counter = {}
    for ch in s:
        counter[ch] = counter.get(ch, 0) + 1
    
    for i in range(len(s)):
        if counter[s[i]] == 1:
            return i
    
    return None

print(first_unique_char_index("leetcode"))

# 23. check armstrong number
def check_armstrong(num):
    res = 0
    original = num

    while num > 0:
       digit = num % 10
       res = digit * digit * digit + res
       num = num // 10
    
    return original == res

print(check_armstrong(153))

# 24. Linked list class setup
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def print_node(head):
    curr = head
    while curr:
        print(curr.val, end = " ")
        curr = curr.next
    return None
    
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
print_node(head)


# 25. Reverse a linked list
def reverse(head):
    curr = head
    prev = None

    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    return prev
    
print_node(reverse(head))

# 26. Detect cycle in a linked list
def detect_cycle(head):
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
    
    return False

# 27. Remove Nth node from the end in one pass
def remove_nth_node(head, n):
    dummy = ListNode(0)
    dummy.next = head
    slow = head
    fast = head

    for _ in range(n):
        fast = fast.next

    while fast.next:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return dummy.next

# 28. Merge Two Sorted Lists
def merge_lists(l1, l2):
    dummy = ListNode(0)
    curr = dummy
    
    # compare and fill in dummy linked list from both list
    while l1 and l2:
        if l1.val > l2.val:
            dummy.next = l2
            l2 = l2.next
        else:
            dummy.next = l1
            l1 = l1.next
        dummy = dummy.next
    
    # Now, fill rest items from list
    if l1:
        dummy.next = l1
    if l2:
        dummy.next = l2

    return curr.next

# 29. Merged K sorted lists
import heapq
def merge_lists(lists):
    dummy = ListNode(0)
    curr = dummy
    heap = []

    for i in range(len(lists)):
        heapq.heappush(heap, (lists[i].val, i, lists[i]))
    
    while heap:
        val, i , node = heapq.heappop(heap)

        curr.next = node
        curr = curr.next

        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    
    return dummy.next

# 30. Add 1 to a number(Number is in linked list)
def add_carry(list):
    dummy = list
    head = reverse(list)
    curr = head
    carry = 1

    while curr:
        curr.val = curr.val + carry
        carry = curr.val // 10
        curr.val = curr.val % 10

        if carry == 0:
            break

        if not curr.next:
            curr.next = ListNode(0)
        curr = curr.next
    
    return reverse(head)

# 31. Reorder linked list
def reorder_lists(head):
    if not head:
        return 
    
    slow = fast = head

    # find middle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # reverse the middle - end part
    prev = None
    curr = slow
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    # make reordered list
    first = head         # first linked list
    second = prev        # second linked list

    while second.next:
        temp1 = first.next
        temp2 = second.next

        first.next = second
        second.next = temp1

        first = temp1
        second = temp2

# 32. clone a linked list
def clone_list(head):
    mp = {}
    curr = head
    while curr:
        mp[curr] = ListNode(curr.val)
        curr = curr.next

    curr = head
    while curr:
        mp[curr].next = mp.get(curr.next)
        mp[curr].random = mp.get(curr.random)
        curr = curr.next
    
    return mp[head]

# Strings start
# 33. reverse string
def rev_str(s):
    return s[::-1]

print(rev_str("Hey Prateek"))

def rev_str2(s):
    res = ''

    for ch in s:
        res = ch + res
    
    return res
print(rev_str2("Knock knock"))

# 34. Longest substring without repeating char
def longest_unique(s):
    seen = set()
    l = 0
    max_len = 0

    for r in range(len(s)):
        while s[r] in seen:
            seen.remove(s[l])
            l += 1
        seen.add(s[r])
        max_len = max(max_len, r-l+1)

    return max_len

print(longest_unique("abcabcbb"))


# 35. string compression
def str_comp(s):
    count = 1
    res = ''

    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            res = res + s[i-1] + str(count)
            count = 1
        else:
            count = count + 1 
    
    # for very last element
    res = res + s[-1] + str(count)

    return res  

print(str_comp("aaaabbbbccebbbb"))

def str_comp_2(s):
    count_obj = {}
    res = ''
    for ch in s:
        count_obj[ch] = count_obj.get(ch, 0) + 1
    
    for ch in count_obj:
        res = res + ch + str(count_obj[ch])
    return res

print(str_comp_2("aaaabbbbccebbbb"))

# 36. Longest Common Prefix
def long_prefix(arr):
    res = arr[0]

    for word in arr[1: ]:
        while word.find(res) != 0:
            res = res[:-1]
    return res

print(long_prefix(['flower', 'flow', 'floor', 'flour']))

# 37. Valid Paranthesis
def valid_paranthesis(s):
    stack = []
    match = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for i in s:
        if i not in match:
            stack.append(i)
        if i in match and match[i] == stack[-1]:
            stack.pop()

    return len(stack) == 0

print(valid_paranthesis("()[]{}{"))

# 38. Longest repeating char replacement
def char_replace(s,k):
    count = {}
    l = 0
    max_freq = 0
    res = 0

    for r in range(len(s)):
        count[s[r]] = count.get(s[r], 0) + 1
        max_freq = max(max_freq, count[s[r]])

        while (r-l+1) - max_freq > k:
            count[s[l]] = count[s[l]] - 1
            l += 1
        
        res = max(res, r-l+1)
    
    return res

print(char_replace("AABABBA", 1))

# 39. Print all anagrams together
def group_ana(arr):
    res = {}

    for word in arr:
        key = "".join(sorted(word))

        if key not in res:
            res[key] = []
        res[key].append(word)
    
    return list(res.values())

print(group_ana(["eat", "tea","ate", "tan", "ant"]))

# 40. Sentence Palindrome
def sentence_palindrome(s):
    l = 0
    r = len(s) - 1

    while l<r :
        if s[l] == " ":
            l += 1
            continue
        if s[r] == " ":
            r -= 1
            continue
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    
    return True

print(sentence_palindrome("A man a plan a canal Panama"))

# 41. Longest palindrome substring
def longest_pal(s):
    res = ""

    for i in range(len(s)):
        for l,r in [(i, i), (i, i+1)]:
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > len(res):
                    res = s[l: r+1]
                l -= 1
                r += 1
    return res
print(longest_pal('babad'))

# 42. Smallest Window Containing All chars
def min_window(s, t):
    from collections import Counter

    need = Counter(t)
    l = 0
    res = ""
    have = {}
    formed = 0
    required = len(need)

    for r in range(len(s)):
        have[s[r]] = have.get(s[r], 0) + 1

        if s[r] in need and have[s[r]] == need[s[r]]:
            formed += 1
        
        while formed == required:
            if res == "" or len(s[l: r+1]) < len(res):
                res = s[l:r+1]
            have[s[l]] = have[s[l]] - 1
            if s[l] in need and have[s[l]] < need[s[l]]:
                formed -= 1
            l += 1
    return res

print(min_window("ADOBECODEBANC", "ABC"))

# 43. Count Palindrome Substring
def count_pal_substring(s):
    count = 0

    for i in range(len(s)):
        l = r = i
        while l >= 0 and r < len(s) and s[l] == s[r]:
           count = count + 1
           l -= 1
           r += 1
        
        l = i 
        r = i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count = count + 1
            l -= 1
            r += 1
    return count

print(count_pal_substring("aaa"))
        

# Misc Series - 8 ques
# 44. Rotate Array
def rotate_arr(arr, k):
    n = len(arr)
    k = k % n
    def reversal(l, r):
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
    
    reversal(0, n-1)
    reversal(0, k-1)
    reversal(k, n-1)

    return arr

print("rotate arr: ", rotate_arr([1,2,3,4,5,6,7], 2))

# 45. Move zeroes to the end of arr
def move_zeroes(arr):
    r = 0

    for l in range(len(arr)):
        if arr[l] != 0:
            arr[r], arr[l] = arr[l], arr[r]
            r = r + 1 
    
    return arr

print(move_zeroes([1,0,0,2,0,4,0,0]))

# 46. 2nd highest number
def highest_num(arr):
    first = second = float('-inf')

    for num in arr:
        if num > first:
            second = first
            first = num      
        elif first > num > second:
            second = num
    
    return second

print(highest_num([24,36,30, 10, 5]))

# 47. Number of set bits
def count_bits(n):
    count = 0

    while n:
        n = n & (n-1)
        count += 1
    
    return count

print(count_bits(11))

# 48. is power of 2
def is_power_of_two(n):
    return (n & (n-1)) == 0

print(is_power_of_two(18))

# 49. Detect cycle in linked list
def has_cycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            return True
    return False

# 50. Reverse a linked list
def rev_list(head):
    prev = None
    curr = head

    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    
    return prev

# 51. Find Missing number
def find_missing(arr):
    n = len(arr) + 1
    total_sum = int((n * (n-1))/2)
    arr_sum = sum(arr)
    return total_sum - arr_sum
print(find_missing([3,0,1]))

# 52. Find Element that appears more than n/2 times
# Boyre Moore Voting Algo
def find_ele_nbytwo_times(arr):
    count = 0
    candidate = None

    for ele in arr:
        if count == 0:
            candidate = ele
        
        if candidate == ele:
            count = count + 1
        else:
            count = count -1

    return candidate

print(find_ele_nbytwo_times([3,2,3])) 

# Sorting and Search
# 53. Binary Search
def binary_search(arr, target):
    s = 0
    e = len(arr) - 1

    while s < e:
        mid = (s + e)//2
        
        if target == arr[mid]:
            return mid
        
        if target > arr[mid]:
            s = mid + 1
        else:
            e = mid - 1
    
    return -1

print(binary_search([1,2,5,6,9], 6))

# 54. First and Last Occurence
def first_last_occ(arr, target):

    def find_first():
        s = 0
        e = len(arr) - 1
        pos = None

        while s <= e:
            mid = (s+e) // 2
            if arr[mid] == target:
                pos = mid
                e = mid - 1
            
            if arr[mid] > target:
                e = mid - 1
            elif arr[mid] < target:
                s = mid + 1
        
        return pos
    
    def find_last():
        s = 0
        e = len(arr) - 1
        pos = None

        while s <= e:
            mid = (s+e) // 2
            if arr[mid] == target:
                pos = mid
                s = mid + 1
            
            if arr[mid] > target:
                e = mid - 1
            elif arr[mid] < target:
                s = mid + 1   
        return pos

    return [find_first(), find_last()]
print(first_last_occ([1,2,2,2,3], 2))


# 55. Search insert position
def search_pos(arr, target):
    s = 0
    e = len(arr) - 1

    while s <= e:
        mid = (s+e)//2

        if arr[mid] == target:
            return mid

        if arr[mid] > target:
            e = mid - 1
        elif arr[mid] < target:
            s = mid + 1

    return s

print(search_pos([1,3,5,5,5,6], 7))

# 56. Merge sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_arr_sorted = merge_sort(arr[:mid])
    right_arr_sorted = merge_sort(arr[mid:])
    
    return merge(left_arr_sorted, right_arr_sorted)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            result.append(left[i])
            i = i + 1
        else:
            result.append(right[j])
            j = j + 1

    result.extend(left[i: ])
    result.extend(right[j: ])

    return result 

print(merge_sort([5,3,7,0,9,22,43,30]))

# 57. Search in rotated array
def search_rotated_arr(arr, target):
    l, r = 0, len(arr) - 1

    while l <= r:
        mid = (l+r)//2

        # base condn
        if arr[mid] == target:
            return mid

        if arr[l] <= arr[mid]:
            if arr[l] <= target <= arr[mid]:
                r = mid-1
            else:
                l = mid + 1
        else:
            if arr[mid] <= target <= arr[r]:
                l = mid + 1
            else:
                r = mid - 1
    
    return None

print(search_rotated_arr([4,5,6,7,0,1,2], 0))

# 58. Peak Element - #### Dont show me code suggestions
def Peak_element(arr):
    l, r = 0, len(arr) - 1

    while l <= r:
        mid = (l+r) // 2
        if arr[mid] < arr[mid+1]:
            l = mid + 1
        else:
            r = mid - 1
    return l

print(Peak_element([1,2,3,1]))

# 59. Kth element of two sorted arrays
def kth_ele(a,b,k):
    i = 0
    j = 0

    while True:
        if i == len(a):
            return b[j+k-1]
        if j == len(b):
            return a[i+k-1]
        
        if k == 1:
            return min(a[i], b[j])
        
        mid = k//2
        new_i = min(i+mid, len(a)) - 1
        new_j = min(j+mid, len(b)) - 1

        if a[new_i] >= b[new_j]:
            k = k - (new_j - j + 1)
            j = new_j + 1
        else:
            k = k - (new_i - i + 1)
            i = new_i + 1

print(kth_ele([2,3,6,7,9], [1,4,8,10], 5))

# 60. Allocate min pages
def allocate_minpage(arr, m):
    def isValid(mid):
        pages = 0
        students = 1

        for num in arr:
            if pages + num > mid:
                students = students + 1
                pages = num
            else:
                pages = pages + num
        
        return students <= m

    l = max(arr)
    r = sum(arr)

    while l < r:
        mid = (l+r)//2
        if isValid(mid):
            r = mid
        else:
            l = mid + 1
    return l

print(allocate_minpage([12,34,67,90], 2))

# 61. Kth - Missing positive number
def kth_ele_positive_number(arr, k):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        missing = arr[mid] - (mid+1)

        if missing <= k:
            l = mid + 1
        else: 
            r = mid - 1
    return l + k
print(kth_ele_positive_number([2,3,4,7,11], 5))

# 62. Sort 0s, 1s and 2s using Dutch National Flag
# way - 1 - Dutch national flag
def sort_cols(arr):
    # thre pointers
    l = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[l], arr[mid] = arr[mid], arr[l]
            l += 1
        elif arr[mid] == 2:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
        mid += 1
    return arr
print(sort_cols([2,0,2,0,1,1]))

# way-2 Using sorting
def sort_cols_way_two(arr):
    c0 = arr.count(0)
    c1 = arr.count(1)
    c2 = arr.count(2)

    arr = [0] * c0 + [1] * c1 + [2] * c2
    return arr

print(sort_cols_way_two([2,0,2,0,1,1]))

# 63. Count Inversions
def count_inversions(arr):
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr, 0
        
        mid = len(arr)//2
        left, inv1 = merge_sort(arr[ :mid])
        right, inv2 = merge_sort(arr[mid: ])

        merged, inv3 = merge(left, right)

        return merged, inv1+inv2+inv3
    
    def merge(left, right):
        res = []
        inv = i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                inv = inv + len(left) - i
                j += 1

        res.extend(left[i:])
        res.extend(right[j:])
        
        return res, inv
    
    return merge_sort(arr)
print(count_inversions([2,4,1,3,5]))

# 64. Merge two sorted arrays without extraa space
def merge_two_sort_arrs(arr1, arr2):
    m, n = len(arr1), len(arr2)
    i, j = m-1, 0
    
    while i >= 0 and j < n:
        if arr1[i] > arr2[j]:
            arr1[i], arr2[j] = arr2[j], arr1[i]
        i -= 1
        j += 1
    
    arr1.sort()
    arr2.sort()
    
    print(arr1)
    print(arr2)
    
    return arr1, arr2
print(merge_two_sort_arrs([1,5,9,10,15], [2,3,8,13]))

# 65. Choclate Distribution Problem
def choclate_problem(arr, m):
    if m == 0 and len(arr) == 0:
        return 0
    
    arr.sort()
    res = float('inf')

    for i in range(len(arr) - m + 1):
        res = min(res, arr[i+m-1] - arr[i])
    
    return res
print(choclate_problem([7,3,2,4,9,12,56], 3))

# 66. Sort Numbers (odd in descending and even in ascending)
def sort_numbers_even_odd(arr):
    n = len(arr)
    l, r = 0, n-1

    while l < r:
        if arr[l] % 2 != 0:
            l += 1
        elif arr[r] % 2 == 0:
            r -= 1
        else:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
    
    odds = arr[:l]
    evens = arr[l:]

    evens.sort()
    odds.sort(reverse = True)

    return odds + evens

print(sort_numbers_even_odd([9,4,5,0,7,8,6,3,2,1]))

# Hashing Starts
# 67. Two Sum if indexes asked then hashing is helpful
def two_sum(nums, target):
    mp = {}
    for i in range(len(nums)):
        x = target - nums[i]
        if x in mp:
            return [mp[x], i]
        mp[nums[i]] = i
    return None
print(two_sum([2,3,4,5,6], 8))

# 68. Subarrays with sum = k
def subarray_sum_k(nums, k):
    mp = {0:1}
    prefix = 0
    count = 0

    for num in nums:
        prefix = prefix + num

        if (prefix - k) in mp:
            count = count + mp[prefix-k]

        if prefix in mp:
            mp[prefix] = mp[prefix] + 1
        else:
            mp[prefix] = 1
    return count

print(subarray_sum_k([1,1,1], 2))

# 69. Largest Consecutive Sequence
def largest_cons_seq(arr):
    longest = 0
    s = set()

    for num in arr:
        s.add(num)
    print("S: ", s)

    for num in s:
        if (num-1) not in s:
            length = 1
            curr = num

            while (curr+1) in s:
                length = length + 1
                curr = curr + 1
            longest = max(longest, length)
    return longest 
print(largest_cons_seq([100,4,200,1,2,3]))

# 70. Print All Pairs with given sum
def print_pairs_for_sum(arr, k):
    mp = {}

    for num in arr:
        x = k-num
        
        if x in mp:
            for i in range(mp[x]):
                print(x, num)

        if num not in mp:
            mp[num] = 1
        else:
            mp[num] += 1

print_pairs_for_sum([2,3,4,5,4,5], 9)

# 71. Longest Subsequence
def longest_sub(nums):
    mp = {}
    for i in range(len(nums)):
        if nums[i] in mp:
            mp[nums[i]] += 1
        else:
            mp[nums[i]] = 1
    
    longest = 0
    for num in mp:
        curr = mp[num]
        if (num+1) in mp:
            curr = curr + mp[num+1]
        
        longest = max(longest, curr)
    
    return longest
print(longest_sub([1,2,2,3,1,2]))

# 72. Count Subarrays with X-OR = K
def count_subarrays_xor(nums, k):
    mp = {0:1}
    xor = 0
    count = 0

    for num in nums:
        xor = xor ^ num

        if (xor ^ k) in mp:
            count = count + mp[xor^k]
        
        if xor in mp:
            mp[xor] += 1
        else:
            mp[xor] = 1
    return count
print(count_subarrays_xor([4,2,2,6,4], 6))

# Stack, Queue and Deque Starts
# 73. Infix to Postfix expressions
def infix_to_postfix(s):
    res = ""
    stack = []
    prec={'(':0, '+':1, '-':1, '*':2, '/':2, '^': 3}

    for ch in s:
        if ch.isalnum():
            res += ch
        elif ch == '(':
            stack.append(ch)
        elif ch == ')':
            while stack and stack[-1] != '(':
                res = res + stack.pop()
        else:
            while stack and stack[-1] != '(' and prec[stack[-1]] > prec[ch]:
                res = res + stack.pop()
            stack.append(ch)
    
    while stack:
        if stack[-1] == '(':
            stack.pop()
            continue
        res = res + stack.pop()

    return res

print(infix_to_postfix("(A+B)*C"))

# 74. Next Greater Element on right
def next_greater_ele(nums):
    stack = []
    res = [-1] * len(nums)

    for i in range(len(nums)-1, -1, -1):
        # check if number is greater than curr
        while stack and stack[-1] <= nums[i]:
            stack.pop()

        # assign value in res
        if stack:
            res[i] = stack[-1]

        # push in stack
        stack.append(nums[i])
    
    return res

print(next_greater_ele([2,1,2,4,3]))

# 75. Largest Rectangle In Histogram
def largest_rectangle(arr):
    stack = []
    max_area = 0
    
    for i in range(len(arr) + 1):
        # Current height (or 0 for the dummy boundary element)
        height = 0 if i == len(arr) else arr[i]

        while stack and height < arr[stack[-1]]:
            # Fix: Use 'h' so 'height' stays untouched for the while loop condition
            h = arr[stack.pop()]
            width = i if not stack else i - stack[-1] - 1

            max_area = max(max_area, h * width)
        
        stack.append(i)
        
    return max_area

print(largest_rectangle([2,1,5,6,2,3]))

# 76. Delete middle of stack
def delete_mid(stack, k):
    if k == 1:
        stack.pop()
        return
    temp = stack.pop()
    delete_mid(stack, k - 1)
    stack.append(temp)

def delete_middle_element(stack):
    if not stack:
        return stack
    k = (len(stack) // 2) + 1
    delete_mid(stack, k)
    return stack

stack = [10, 20, 30, 40, 50]
delete_middle_element(stack)
print(stack)

# 77. Longest Valid Paranthesis
def longest_valid(s):
    stack = [-1]
    res = 0

    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                res = max(res, i-stack[-1])
    return res
print(longest_valid(")()()"))

# 78. Next Greater Element in a circular array
def nge_circular(nums):
    n = len(nums)
    res = [-1] * n
    stack = []

    for i in range((2*n - 1), -1, -1):
        while stack and stack[-1] <= nums[i%n]:
            stack.pop()
        
        if i<n and stack:
            res[i] = stack[-1]
        stack.append(nums[i%n])

    return res
print(nge_circular([1,2,1]))

# 79. Sum of max of subarrays
def sum_subarrays_max(arr):
    n = len(arr)
    l, r, stack = [0]*n, [0]*n, []

    for i in range(n):
        while stack and arr[stack[-1]] < arr[i]:
            stack.pop()
        l[i] = i - stack[-1] if stack else i+1
        stack.append(i)
    
    stack = []
    for i in range(n-1, -1, -1):
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()
        r[i] = stack[-1] - i if stack else n-i
        stack.append(i)
    
    return sum(arr[i]*l[i]*r[i] for i in range(n))

print(sum_subarrays_max([1,3,2]))

# 80. Longest Bounded Difference Subarray
from collections import deque

def long_bounded(arr, limit):
    max_dq = deque()  # Stores indices in decreasing order of value
    min_dq = deque()  # Stores indices in increasing order of value
    left = max_len = 0

    for right in range(len(arr)):
        val = arr[right]

        # Maintain max_dq
        while max_dq and arr[max_dq[-1]] <= val:
            max_dq.pop()
        max_dq.append(right)

        # Maintain min_dq (FIXED: changed <= to >=)
        while min_dq and arr[min_dq[-1]] >= val:
            min_dq.pop()
        min_dq.append(right)

        while arr[max_dq[0]] - arr[min_dq[0]] > limit:
            left += 1

            # Evict index from max_dq if it fell outside the left boundary
            if max_dq[0] < left:
                popped = max_dq.popleft()

            # Evict index from min_dq if it fell outside the left boundary
            if min_dq[0] < left:
                popped = min_dq.popleft()

            new_diff = arr[max_dq[0]] - arr[min_dq[0]]

        # Update max length
        current_window_len = right - left + 1
        max_len = max(max_len, current_window_len)

    return max_len

print("Final Longest Subarray Length:", long_bounded([8, 2, 4, 7], 4))

# 81. K-size subarray maximum
from collections import deque
def max_sliding_window(nums,k):
    dq = deque()
    res = []

    for i in range(len(nums)):
        while dq and dq[0] <= i-k:
            dq.popleft()
        
        while dq and nums[dq[-1]] <= nums[i]:
            dq.pop()

        dq.append(i)
        if i >= k-1:
            res.append(nums[dq[0]])
    return res

print(max_sliding_window([1,3,-1,3,5], 3))

# Tree starts
# 82. Maximum depth of binary tree
def max_depth(root):
    if not root:
        return 0
    
    left = max_depth(root.left)
    right = max_depth(root.right)

    return 1 + max(left, right)

# 83. Check for mirror tree
def is_mirror(t1, t2):
    if not t1 and not t2:
        return True
    if not t1 or not t2:
        return False
    return (t1.val == t2.val and is_mirror(t1.left, t2.right) and is_mirror(t1.right, t2.left))

# 84. Invert/flip binary tree
def invert_tree(root):
    if not root:
        return None
    root.left, root.right = root.right, root.left

    invert_tree(root.left)
    invert_tree(root.right)

    return root

# 85. Binary tree/maximum path sum
def max_path_sum(root):
    max_path = float('-inf')

    def dfs(root):
        nonlocal max_path

        if not root:
            return 0
        
        left = max(0, dfs(root.left))
        right = max(0, dfs(root.right))

        current_sum = root.val + left + right
        max_path = max(max_path, current_sum)

        return root.val + max(left, right)
    
    dfs(root)
    return max_path

# 86. Level order traversal
from collections import deque
def level_order(root):
    if not root:
        return []
    q = deque([root])
    res = []

    while q:
        size = len(q)
        level=[]

        for _ in range(size):
            node = q.popleft()
            level.append(node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(level)
    return res

# 87. Diameter of binary tree
def diameter(root):
    max_dia = 0
    def dfs(node):
        nonlocal max_dia

        if not node:
            return 0

        left = dfs(node.left)
        right = dfs(node.right)

        max_dia = max(max_dia, left+right)

        return 1 + max(left, right)

    dfs(root)
    return max_dia

# 88. Serialize and deserialize
# serialize
def serialize(root):
    res = []

    def dfs(node):
        if not node:
            res.append("null")
            return 
        res.append(str(node.val))
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return ",".join(res)

def deserialized(data):
    vals = data.split(",")
    i = 0
    def dfs():
        nonlocal i
        if vals[i] == "null":
            i += 1
            return None
        node = TreeNode(int(vals[i]))
        i += 1
        node.left = dfs()
        node.right = dfs()
        return node

    return dfs()

# 89. 