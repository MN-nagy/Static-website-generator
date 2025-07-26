"""
->> Binary Search Trees <BST>:
1. each node has at most 2 children.

2. the left child's value must be less than it's parent's value.

3. the right child's value must grater than it's parent's value.

4. no two nodes in the BST can have the same value.
"""


class BSTNode:
    def height(self):
        if self.val is None:
            return 0
        left_height = self.left.height() if self.left else 0
        right_height = self.right.height() if self.right else 0
        return 1 + max(left_height, right_height)

    # don't touch below this line

    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)
