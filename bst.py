class Node(object):
        def __init__(self, val, parent=None, left=None, right=None):
            self.val = val
            self.parent = parent
            self.left = left
            self.right = right


class BST(object):
    def __init__(self, val=None):
        if val is not None:
            self.root = Node(val)
        else:
            self.root = None

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

    def _find(self, val):
        """Return a tuple containing (node, side) with target val if it exists,
        otherwise return the would be parent and 1 if it is on the left, -1 if
        it is on the right, 0 if it is the root."""

        def _look(node):
            if node.val > val:
                if node.left is not None:
                    self._find(node.left)
            elif node.val < val:
                if node.right is not None:
                    self._find(node.right)
            return node

        if self.root is not None:
            return _look(self.root)
        else:
            return None
