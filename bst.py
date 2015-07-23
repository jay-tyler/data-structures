class Node(object):
        def __init__(self, val, parent=None, left=None, right=None):
            self.val = val
            self.parent = parent
            self.left = left
            self.right = right

        def __repr__(self):
            return ("Node({self.val},"\
                    "left={self.left}, right={self.right})".format(self=self))


class BST(object):
    def __init__(self, val=None):
        self._size = 0
        self.root = None
        if val is not None:
            self.insert(val)
        else:
            self.root = None

    def insert(self, val):
        """Insert val into BST if not present. Always returns None."""
        if self.root is None:
            self.root = Node(val)
            self._size += 1
        else:
            new_parent = self._find(val)
            if new_parent.val > val:
                new_parent.left = Node(val, new_parent)
                self._size += 1
            elif new_parent.val < val:
                new_parent.right = Node(val, new_parent)
                self._size += 1
            else:
                return

    def contains(self, val):
        """Return True if val in BST. Else, return False."""
        pass

    def size(self):
        """Return int size of tree. Will return 0 if tree is empty."""
        return self._size

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
        if self.root is not None:
            l, r = self.lr_levels()
            return l - r
        else:
            return 0

    def _find(self, val):
        """Return a tuple containing (node, side) with target val if it exists,
        otherwise return the would be parent and 1 if it is on the left, -1 if
        it is on the right, 0 if it is the root."""

        def _look(node):
            if node.val > val:
                if node.left is not None:
                    return _look(node.left)
            elif node.val < val:
                if node.right is not None:
                    return _look(node.right)
            return node

        if self.root is not None:
            return _look(self.root)
        else:
            return None

    def lr_levels(self):
        # import pdb; pdb.set_trace()
        def _levels(node):
            l, r = 0, 0
            if node.left is not None:
                l = _levels(node.left)
            if node.right is not None:
                r = _levels(node.right)
            if l > r:
                return l + 1
            else:
                return r + 1

        if self.root is None:
            return None
        w_left, w_right = 0, 0
        if self.root.left is not None:
            w_left = _levels(self.root.left)
        if self.root.right is not None:
            w_right = _levels(self.root.right)
        return w_left, w_right


def test_helper():
    A = Node(5)
    B = Node(4, parent=A)
    C = Node(6, parent=A)
    D = Node(3, parent=B)
    E = Node(2, parent=B)
    F = Node(7, parent=C)

    # Backrefs
    A.left = B
    A.right = C
    B.left = D
    B.right = E
    C.right = F

    return [A, B, C, D, E, F]
