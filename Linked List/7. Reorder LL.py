# Time: O(n), Space: O(1)

# i/p: [1->2->3->4->5]
# o/p: [1->5->2->4->3]

def reorder(head):
    if not head:
        return
    slow = fast = head

    # slow at the mid point (become two LL -> L1 and L2)
    while fast.next:
        slow = slow.next
        fast = fast.next.next

    # reverse the LL2 (mid point to end)
    prev = None
    curr = slow
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    
    # merge both LL1 and LL2
    first = head
    second = prev

    while second.next:
        temp1 = first.next
        temp2 = second.next

        first.next = second
        second.next = temp1

        first = temp1
        second = temp2
        
    
