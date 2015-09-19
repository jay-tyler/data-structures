from __future__ import unicode_literals
from itertools import chain


class Node(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return "Node({})".format(self.val)

    def __str__(self):
        """Print representation of node."""
        return "{val}".format(val=self.val)


class LinkedList(object):
    """Class for a singly-linked list."""

    def __init__(self, iterable=()):
        self._current = None
        self.head = None
        self.length = 0
        for val in reversed(iterable):
            self.insert(val)

    def __repr__(self):
        return "LinkedList({})".format(list(self.itervals()))

    def __str__(self):
        """Print representation of LinkedList."""
        node = self.head
        output = ""
        for node in self:
            output += "{!r}, ".format(node.val)
        return "({})".format(output.rstrip(' ,'))

    def __len__(self):
        return self.length

    def __iter__(self):
        if self.head is not None:
            self._current = self.head
        return self

    def __next__(self):
        """For Py 3.x compatibility"""
        self.next()

    def next(self):
        if self._current is None:
            raise StopIteration
        node = self._current
        self._current = self._current.next
        return node

    def itervals(self):
        """Generate alternative iterator that serves each node.val"""
        for node in iter(self):
            yield node.val

    def __add__(self, other):
        """Concatenate two LinkedLists together"""
        sumvals = chain(self.itervals(), other.itervals())
        return LinkedList(list(sumvals))

    def insert(self, val):
        """Insert value at head of LinkedList.

        args:
            val: the value to add
        """
        self.head = Node(val, self.head)
        self.length += 1
        return None

    def pop(self):
        """Pop the first val off the head and return it."""
        if self.head is None:
            raise IndexError
        else:
            to_return = self.head
            self.head = to_return.next
            self.length -= 1
            return to_return.val

    def size(self):
        """Return current length of LinkedList."""
        return len(self)

    def search(self, search_val):
        """Return the node containing val if present, else None.

        args:
            search_val: the value to search by

        returns: a node object or None
        """
        for node in self:
            if node.val == search_val:
                return node
        else:
            return None

    def remove(self, search_node):
        """Remove given node from list, return None.

        args:
            search_node: the node to be removed
        """
        for node in self:
            if node.next == search_node:
                node.next = node.next.next
                return None

    def display(self):
        """Shows str representation of LinkedList."""
        return str(self)
