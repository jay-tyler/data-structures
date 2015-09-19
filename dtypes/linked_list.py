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
        # TODO:Rewrite
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

    def __list__(self):
        """Akin to self.__dict__; return a list form representation of LinkedList"""
        return list(self.itervals())

    def __contains__(self, val):
        return val in set(self.itervals())

    def __add__(self, other):
        """Concatenate two LinkedLists together"""
        sumvals = chain(self.itervals(), other.itervals())
        return LinkedList(list(sumvals))

    def __iadd__(self, other):
        """Concatenate in-place

        Slightly expensive implementation, but alas, no way to reverse
        an iterator"""
        vals = self.__list__()
        for val in reversed(vals):
            self.insert(val)
        return self

    def copy(self):
        return LinkedList(self.__list__())

    def insert(self, val):
        """Insert value at head of LinkedList.

        args:
            val: the value to add
        """
        self.head = Node(val, self.head)
        return None

    def pop(self):
        """Pop the first val off the head and return it."""
        if self.head is None:
            raise IndexError
        else:
            to_return = self.head
            self.head = to_return.next
            return to_return.val

    def append(self, val):
        """Insert an item at end of LinkedList

        This is mildly expensive as n-nodes must be traversed"""
        for node in iter(self):
            prev = node
        prev.next = Node(val)

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
