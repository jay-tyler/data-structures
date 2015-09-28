# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from linked_list import LinkedList, Node


class Queue(LinkedList):

    def __init__(self, iterable=()):
        super(Queue, self).__init__(iterable)
        self.tail = self[-1] if len(self) > 0 else None

    #TODO replace __repr__ and __str__
    
    def enqueue(self, value):
        """Add a value to the tail of a queue.

        args:
            value: The value to add to the queue
        """
        new_node = Node(value)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        """Remove and return a value from the head of the queue."""
        if len(self) == 1:
            self.tail = None
        return self.pop()

    def size(self):
        return len(self)
