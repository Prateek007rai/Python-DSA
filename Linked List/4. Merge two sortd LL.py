# Merge two sorted LL -> sorted one
# Time: O(n+m), Space: O(1)

# i/p: 1->3->5, 2->4->6
# o/p: 1->2->3->4->5->6

def merge_two_LL(list1, list2):

    dummy= ListNode(0)
    curr = dummy

    while list1 and list2:
        if list1.val < list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next
        curr = curr.next
    
    # if left in any of LL
    curr.next = list1 if list1 else list2

    return dummy.next