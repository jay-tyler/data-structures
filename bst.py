class Node(object):
        def __init__(self, val, parent=None, left=None, right=None):
            self.val = val
            self.parent = parent
            self.left = left
            self.right = right

        def __repr__(self):
            return ("Node({self.val}, parent={self.parent},"\
                    "left={self.left}, right={self.right})".format(self=self))


class BST(object):
    def __init__(self, val=None):
        self.root = Node(val)

    def insert(self, val):
        """Insert val into BST if not present. Always returns None."""
        pass

    def contains(self, val):
        """Return True if val in BST. Else, return False."""
        pass

    def size(self):
        """Return int size of tree. Will return 0 if tree is empty."""
        pass

    def depth(self):
        """Return the int number of levels in the tree.
        Return 0 if tree is empty."""
        pass

    def balance(self):
        """Return the difference between the number of nodes on the left with
        respect to the right side.
        --Negative if more on right
        --Positive if more on left
        --Zero if tree is perfectly balanced"""
        pass

    def _find(self, root, val):
        """Return a tuple containing (node, side) with target val if it exists,
        otherwise return the would be parent and 1 if it is on the left, -1 if
        it is on the right, 0 if it is the root."""

        def _look(node):
            if root.val > val:
                if root.left is not None:
                    self._find(root.left, val)
            elif root.val < val:
                if root.right is not None:
                    self._find(root.right, val)
            return node

        if self.root is not None:
            return _look(self.root)


def test_helper():
    A = Node(5)
    B = Node(4, parent=A)
    C = Node(6, parent=)