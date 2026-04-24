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