# Time: O(n * log k), space: O(k)

# i/p: [1->4->5, 1->3->4, 2->6]
# o/p: [1->1->2->3->4->4->5->6]

import heapq

def merge_lls(lists):
    dummy = ListNode(0)
    curr = dummy
    heap = []

    # put each first node (head) in min-heap
    for i in range(len(lists)):
        heapq.heappush(heap, (list[i].val, i, list[i]))

    # merge and store in dummy
    while heap:
        val, i , node = heapq.heappop(heap)
        curr.next = node
        curr = curr.next

        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    
    return dummy.next
