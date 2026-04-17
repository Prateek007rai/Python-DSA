# Also known as Floyd's alogrithm (Using Two pointer technique) || Tortoise and the Hare Problem
# Time: O(n), Space: O(1)

# i/p: 1->2->3->4->2
# o/p: True


def detect_cycle(head):
    
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
    
    return False
    
