# -*- coding: utf-8 -*-
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
    """Class for a singly-linked list without loops."""

    def __init__(self, iterable=()):
        self._current = None
        self.head = None
        for val in reversed(iterable):
            self.insert(val)

    def __repr__(self):
        return "LinkedList({})".format(self.__list__())

    def __str__(self):
        """Print representation of LinkedList."""
        node = self.head
        output = ""
        for node in self:
            output += "{!r}, ".format(node.val)
        return "({})".format(output.rstrip(' ,'))

    def __len__(self):
        prev = None
        for i, val in enumerate(self):
            prev = i
        return prev + 1 if prev is not None else 0

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
        for node in self:
            yield node.val

    def __list__(self):
        """Return a list form representation of LinkedList

        Akin to self.__dict__"""
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
        self.extend(other.__list__())
        return self

    def __mul__(self, n):
        iterable = []
        for i in range(n):
            iterable += self.__list__()
        return LinkedList(iterable)

    def __rmul__(self, n):
        return self.__mul__(self, n)

    def __imul__(self, n):
        for i in range(1, n):
            self.extend(self.__list__())
        return self

    def __getitem__(self, index):
        for i, node in enumerate(self):
            if i == index:
                return node
            elif not node.next:
                return node if index == -1 else None

    def __delitem__(self, index):
        pop(index)

    def copy(self):
        return LinkedList(self.__list__())

    def extend(self, iterable):
        """Add values in iterable to end of LinkedList"""
        for val in iterable:
            self.append(val)
        return self

    def count(self, val):
        count = 0
        for node in self:
            if node.val == val:
                count += 1
        return count

    def index(self, val):
        for i, node in enumerate(self):
            if node.val == val:
                return i

    def clear(self):
        self._current = None
        self.head = None

    def insert(self, val):
        #TODO: Refactor to do insert(position, val)
        """Insert value at head of LinkedList.

        args:
            val: the value to add
        """
        self.head = Node(val, self.head)
        return None

    def pop(self, index=0):
        """Pop the first val off the head and return it."""
        if self.head is None:
            raise IndexError
        else:
            to_return = self[index]
        if index == 0:
            self.head = to_return.next
        return to_return.val

    def append(self, val):
        """Insert an item at end of LinkedList

        This is mildly expensive as n-nodes must be traversed"""
        for node in self:
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
        #TODO: remove by value
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

    def sort(self, key=None, reverse=False):
        #TODO
        pass

    def __reversed__(self):
        #TODO
        pass

    def reverse(self):
        #TODO
        pass
