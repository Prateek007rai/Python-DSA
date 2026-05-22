# 3 Pointer technique
# Time: O(n), Space: O(1)




def reverse_list(head):
    prev = None
    curr = head
    
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    
    return prev
    
