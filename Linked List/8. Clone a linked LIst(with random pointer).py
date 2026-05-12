# Time: O(n), Space: O(n)

# Input: Nodes: 1, 2, 3
# Pointers: (1.next=2, 1.rand=3), (2.next=3, 2.rand=1), (3.next=None, 3.rand=2)

# Output:
# A completely new set of memory addresses for nodes 1, 2, 3 with the exact same value and pointer relationships as the input.


def clone_LL(head):
   

    mp={}
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
