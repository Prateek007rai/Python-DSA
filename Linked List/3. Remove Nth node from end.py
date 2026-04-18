# Remove nth node from end
# Time: O(n), Space: O(1)
# i/p: 1->2->3->4->5, n= 2
# o/p: 1->2->3->5

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_nth(head, n):
    dummy = ListNode(0)                   # Handle head removal
    dummy.next = head
    slow = fast = dummy

    for _ in range(n + 1):                      # Create n+1 gap
        fast = fast.next

    while fast:                                 # Move slider
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next                  # Delete target
    return dummy.next                           # Return new head
