# Use three pointer method - prev, curr and next 
# Time complexity - O(n)
# Space complexity - O(1)

class ListNode:
    def __init__(self, x):
        self.value = x
        self.next = None
        
node1 = ListNode(3)
node2 = ListNode(0)
node3 = ListNode(-4)
node4 = ListNode(7)

node1.next = node2
node2.next = node3
node3.next = node4


# display linked list
def display(head):
    curr = head
    while curr:
        print(curr.value, end= " ")
        curr = curr.next
    return print(None)


# get nth node
# Example: get_nth(head, 2) on 10 -> 20 -> 30
# Output: 30
def nth_node(head, n):
    curr = head
    count = 0
    
    while curr:
        if count == n:
            return curr.value
        curr = curr.next
        count += 1
        
    print("Index out of bound")


# using 3 pointers
def reverse(head):
    prev = None
    curr = head
    
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
        
    display(prev)        #bcz curr is current head 
    return True
  
print("3rd node: ", nth_node(node1, 2))  
print("is Reversed? ", reverse(node1))


