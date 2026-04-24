class SimpleTree:
    def __init__(self):
        self.tree = []

    def insert_at(self, index, value):
        while len(self.tree) <= index:
            self.tree.append(None)
        self.tree[index] = value

    def get_left_child(self, index):
        left_idx = (2 * index) + 1
        if left_idx < len(self.tree):
            return self.tree[left_idx]
        return None

    def get_right_child(self, index):
        right_idx = (2 * index) + 2
        if right_idx < len(self.tree):
            return self.tree[right_idx]
        return None
    
    def get_tree(self):
        return self.tree
    
# --- Main Logic ---
my_tree = SimpleTree()

my_tree.insert_at(0, 10)  # Root
my_tree.insert_at(1, 5)   # Left of 10
my_tree.insert_at(2, 15)  # Right of 10
my_tree.insert_at(3, 2)   # Left of 5

print("Array View:", my_tree.tree)
print("Root:", my_tree.tree[0])
print("Left Child of 10:", my_tree.get_left_child(0))
print("Right Child of 10:", my_tree.get_right_child(0))

print("Whole tree: ", my_tree.get_tree())