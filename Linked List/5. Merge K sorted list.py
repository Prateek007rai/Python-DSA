# Time: O(n * log k), space: O(k)

# i/p: [1->4->5, 1->3->4, 2->6]
# o/p: [1->1->2->3->4->4->5->6]

import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val                                  # Node value
        self.next = next                                # Pointer to next

# --------------------------------------------------- Main code starts ------------------------------------------------
def merge_lls(lists):
    dummy = ListNode(0)                                 # Result placeholder
    curr = dummy
    heap = []

    for i in range(len(lists)):
        if lists[i]:                                    # Check if list is not empty
            heapq.heappush(heap, (lists[i].val, i, lists[i]))

    while heap:
        val, i, node = heapq.heappop(heap)              # Get smallest node
        curr.next = node                                # Link to result
        curr = curr.next                                # Move result pointer

        if node.next:                                   # If more nodes in that list
            heapq.heappush(heap, (node.next.val, i, node.next))
    
    return dummy.next

# --------------------------------------------------- Main code ends ------------------------------------------------

# --- HELPER FUNCTIONS TO RUN LOCALLY ---

def create_ll(arr):
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def print_ll(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# --- EXECUTION ---
if __name__ == "__main__":
    # Create 3 sorted linked lists
    l1 = create_ll([1, 4, 5])
    l2 = create_ll([1, 3, 4])
    l3 = create_ll([2, 6])

    # Run the merge
    merged_head = merge_lls([l1, l2, l3])

    # Print the result
    print_ll(merged_head)                               # 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6 -> None
