# Use two pointer method - Slow and fast 
# Floyd's cycle detection algo
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

# for cycle move its next to 2nd for cycle
node4.next = node2


# Main cycle detection function
def hasCycle(head):
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
           return True
    return False

print(hasCycle(node1))                #just pass the head

