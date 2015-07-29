import random
from timeit import default_timer
from queue import Queue


class Node(object):
        def __init__(self, val, parent=None, left=None, right=None):
            self.val = val
            self.parent = parent
            self._left = left
            self._right = right

        @property
        def left(self):
            return self._left

        @property
        def right(self):
            return self._right

        @left.setter
        def left(self, val):
            self._left = Node(val, self)

        @right.setter
        def right(self, val):
            self._right = Node(val, self)

        def __repr__(self):
            return ("Node({self.val}, parent={self.parent})".format(self=self))

        def get_dot(self):
            """return the tree with root 'self' as a dot graph for visualization"""
            return "digraph G{\n%s}" % ("" if self.val is None else (
                "\t%s;\n%s\n" % (
                    self.val,
                    "\n".join(self._get_dot())
                )
            ))

        def _get_dot(self):
            """recursively prepare a dot graph entry for this node."""
            if self.left is not None:
                yield "\t%s -> %s;" % (self.val, self.left.val)
                for i in self.left._get_dot():
                    yield i
            elif self.right is not None:
                r = random.randint(0, 1e9)
                yield "\tnull%s [shape=point];" % r
                yield "\t%s -> null%s;" % (self.val, r)
            if self.right is not None:
                yield "\t%s -> %s;" % (self.val, self.right.val)
                for i in self.right._get_dot():
                    yield i
            elif self.left is not None:
                r = random.randint(0, 1e9)
                yield "\tnull%s [shape=point];" % r
                yield "\t%s -> null%s;" % (self.val, r)


class BST(object):
    def __init__(self, val=None):
        self._size = 0
        self.root = None
        if val is not None:
            self.insert(val)

    def insert(self, val):
        """Insert val into BST if not present. Always returns None."""
        if self.root is None:
            self.root = Node(val)
        else:
            new_parent = self._find(val)
            if new_parent.val > val:
                new_parent.left = val
            elif new_parent.val < val:
                new_parent.right = val
            else:
                return
        self._size += 1

    def contains(self, val):
        """Return True if val in BST. Else, return False."""
        checkdis = self._find(val)
        try:
            return checkdis.val == val
        except AttributeError:
            return False

    def size(self):
        """Return int size of tree. Will return 0 if tree is empty."""
        return self._size

    def depth(self):
        """Return the int number of levels in the tree.
        Return 0 if tree is empty."""
        if self.root is not None:
            l, r = self._lr_levels()
            return max([l, r]) + 1
        else:
            return 0

    def balance(self):
        """Return the difference between the number of nodes on the left with
        respect to the right side.
        --Negative if more on right
        --Positive if more on left
        --Zero if tree is perfectly balanced"""
        if self.root is not None:
            l, r = self._lr_levels()aww
            return l - r
        else:
            return 0

    def _find(self, val):
        """Return a tuple containing (node, side) with target val if it exists,
        otherwise return the would be parent and 1 if it is on the left, -1 if
        it is on the right, 0 if it is the root."""
        # Can't remember if we changed our minds or forgot to implement this.
        """Return the node with target val if it exists, otherwise return the
        would be parent."""

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

    def _lr_levels(self):
        def _levels(node):
            l, r = 0, 0
            if node.left is not None:
                l = _levels(node.left)
            if node.right is not None:
                r = _levels(node.right)
            return max([l, r]) + 1

        if self.root is None:
            return None
        w_left, w_right = 0, 0
        if self.root.left is not None:
            w_left = _levels(self.root.left)
        if self.root.right is not None:
            w_right = _levels(self.root.right)
        return w_left, w_right

    def in_order(self):
        """Return a generator that will return the values in the
        tree using in-order traversal, one at a time."""
        def go(n):
            if n is None:
                return
            for node in go(n.left):
                yield node
            yield n
            for node in go(n.right):
                yield node
        for node in go(self.root):
            yield node.val

    def pre_order(self):
        """Return a generator that will return the values in the
        tree using pre-order traversal, one at a time."""
        def go(n):
            if n is None:
                return
            yield n
            for node in go(n.left):
                yield node
            for node in go(n.right):
                yield node
        for node in go(self.root):
            yield node.val

    def post_order(self):
        """Return a generator that will return the values in the
        tree using post_order traversal, one at a time."""
        def go(n):
            if n is None:
                return
            for node in go(n.left):
                yield node
            for node in go(n.right):
                yield node
            yield n
        for node in go(self.root):
            yield node.val

    def breadth_first(self):
        """Return a generator that will return the values in the
        tree using breadth-first traversal, one at a time."""

        def go(n):
            if self.root is not None:
                todo = Queue([self.root])
                while len(todo) > 0:
                    n = todo.dequeue()
                    yield n
                    if n.left is not None:
                        todo.enqueue(n.left)
                    if n.right is not None:
                        todo.enqueue(n.right)
        for node in go(self.root):
            yield node.val

    def delete(self, val):
        """Delete node corresponding to val"""
        target = self._find(val)
        # Check here that target.val is val; don't go into cases below if so
        if target.val != val:
            # Case of not finding val in tree
            return None

        def _adj_pred(node):
            """Return the node with the nearest precedecessor val"""
            pass

        def _del_target(node):
            """Delete node, if node has one or zero children"""
            child = None

            # Checking for children of node
            if node._left is not None:
                left_c = True
                child = node._left
            else:
                left_c = False
            if node._right is not None:
                right_c = True
                child = node._right
            else:
                right_c = False
            if left_c and right_c:
                raise ValueError("Deleted node can have one or zero children")

            # Delete root of tree
            if node.parent is None:
                child.parent = None
                self.root = child
            # Get linkage of parent to node; link parent to child to skip over
            # node
            elif node.parent._left == node:
                node.parent._left, child.parent = child, node.parent
            elif node.parent._right == node:
                node.parent._right, child.parent = child, node.parent

        # Case 1 and 2: Node has zero children or one child

        # Case 3: Node has two children


if __name__ == '__main__':
    # Worst case senerio, the BST is completely unbalanced:
    # either:
    # --the root is the smallest item and you are searching
    # for an item bigger than the biggest item in the BST, or
    # --the root is the biggest item and you are searching
    # for an item smaller than the smallest item in the list.
    BST1 = BST()
    for x in range(51):
        BST1.insert(x)
    start = default_timer()
    for x in range(10000):
        BST1.contains(51)
    print BST1.contains(51)
    end = default_timer()
    print str(end - start) + "<-- Quite a while!"
    # Best case senario, the item you are looking for is the item at root.
    BST2 = BST(1)
    start = default_timer()
    for x in range(10000):
        BST2.contains(1)
    print BST2.contains(1)
    end = default_timer()
    print str(end - start) + "<-- Quite fast!"
    # Or that the tree is well balanced.
    BST3 = BST()
    l = [50, 25, 75, 12, 37, 63, 87, 6, 18, 31, 43, 57, 69, 81, 93, 3, 9, 15,
         21, 28, 34, 40, 46, 54, 60, 66, 72, 78, 84, 90, 96, 1, 4, 8, 10, 14,
         6, 20, 22, 27, 29, 39, 41, 59, 61, 65, 67, 77, 79, 89, 91]
    for x in l:
        BST3.insert(x)
    start = default_timer()
    for x in range(10000):
        BST2.contains(101)
    print BST3.contains(101)
    end = default_timer()
    print str(end - start) + "<-- Fast Enough!"
