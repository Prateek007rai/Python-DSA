# Time: O(n.log k), Space: O(k)

# i/p: [linked_list_0, linked_list_1,linked_list_2]  
# o/p: [single linked list]


import heapq

def merge_k_sorted_lls(lists):
    heap = []

    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(heap, (lists[i].val, i, lists[i]))
    
    dummy = ListNode(0)
    curr = dummy

    while heap:
        val, i ,node = heapq.heappop(heap)

        curr.next = node
        curr = curr.next

        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    
    return dummy.next