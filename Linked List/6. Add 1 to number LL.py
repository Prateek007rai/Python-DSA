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

        if not curr.next and carry > 0:
            curr.next = ListNode(0)               # create  a new list node
        curr = curr.next

    return reverse_list(head)






# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# def reverse_list(head):
#     prev = None
#     curr = head
#     while curr:
#         next_node = curr.next
#         curr.next = prev
#         prev = curr
#         curr = next_node
#     return prev

# def add_one(head):
#     head = reverse_list(head)
#     curr = head
#     carry = 1

#     while curr:
#         curr.val += carry
#         carry = curr.val // 10
#         curr.val %= 10
        
#         if carry == 0:
#             break
            
#         if not curr.next and carry > 0:
#             curr.next = ListNode(0)
            
#         curr = curr.next

#     return reverse_list(head)

# def create_ll(arr):
#     dummy = ListNode(0)
#     curr = dummy
#     for val in arr:
#         curr.next = ListNode(val)
#         curr = curr.next
#     return dummy.next

# def print_ll(head):
#     curr = head
#     while curr:
#         print(curr.val, end=" -> " if curr.next else "")
#         curr = curr.next
#     print()

# if __name__ == "__main__":
#     test_input = [1, 9, 9]
#     head = create_ll(test_input)
    
#     print("Input:")
#     print_ll(head)
    
#     result = add_one(head)
    
#     print("Output:")
#     print_ll(result)