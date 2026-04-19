# Time: O(n), spac: O(1)

# i/p: 1->9->9
# o/p: 2->0->0

def add_one(head):
     
    head = reverse_list(head)
    curr = head
    carry = 1

    while curr:
        curr.val = curr.val + carry
        carry = curr.val // 10                    # 10//10 = 1
        curr.val = curr.val % 10                  # 10 % 10 = 0

        if carry == 0:
            break

        if curr.next == None:
            curr.next = ListNode(0)               # create  a new list node
        curr = curr.next

    return reverse_list(head)
