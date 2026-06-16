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
