# Create a node in py and travere it


class LinkedList: 
    def __init__(self, val):
        self.val = val
        self.next = None

def traverse(head):
    curr = head

    while curr:
        print(curr.val, end="->")
        curr = curr.next

    return print("None")


Node1 = LinkedList(1)
Node2 = LinkedList(2)
Node3 = LinkedList(3)
Node4 = LinkedList(4)

# Currently they are independent nodes, Now Form  LL:
Node1.next = Node2
Node2.next = Node3
Node3.next = Node4

traverse(Node1)
