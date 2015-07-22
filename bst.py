class Node(object):
        def __init__(self):
            self.val = None
            self.parent = None
            self.left = None
            self.right = None


class BST(object):
    def __init__(self, val=None):
        self.root = Node(val)

    def insert(self, val):
        """Insert val into BST if not present. Always returns None."""

    def contains(self, val):
        """Return True if val in BST. Else, return False."""

    def size(self):
        """Return int size of tree. Will return 0 if tree is empty."""

    def depth(self):
        """Return the int number of levels in the tree.
        Return 0 if tree is empty."""

    def balance(self):
        """Return the difference between the number of nodes on the left with
        respect to the right side.
        --Negative if more on right
        --Positive if more on left
        --Zero if tree is perfectly balanced"""

    def _find(self, root, val):
        """Return a tuple containing (node, side) with target val if it exists,
        otherwise return the would be parent and 1 if it is on the left, -1 if
        it is on the right, 0 if it is the root."""

        def _look(node):
            if node.val > val:
                if node.left is not None:
                    self._find(node.left, val)
            elif node.val < val:
                if node.right is not None:
                    self._find(node.right, val)
            return node

        if self.root is not None:
            return _look(self.root)
