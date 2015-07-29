#Data Structures
Implementation of LinkedList and Stack data structures in Python.

##LinkedList
The LinkedList class is composed of a Node base class.

Available methods inlude:
* insert(val)
* pop()
* size()
* search(val)
* remove(node)
* display()

##Stack
The Stack data class is a first-in-first-out data structure built via composition from LinkedList.
Available methods include:
* push(value)
* pop()

##Queue
The Queue data class is a first-in-last-out data structure built via encapsulation of a LinkedList.

Available methods inlude:
* enqueque(value)
* dequeque()
* len()

##Binary Heap
The Binary Heap data class is a binary tree data structure built implemented on a built-in Python
list. The binary heap default to a minheap sort, meaning that the smallest values will be sorted to
the top of the heap. Alternatively, the binary heap can be instantiated as a maxheap so that the
greatest values will be sorted to the top.

Available methods include:
* pop()
* push()

See the doc strings for implementation details.

##PriorityQ
The PriorityQ data class is a binary tree that implements sorting primarily by priority value and
secondarily by insertion order. The PriorityQ defaults to minheap sorting for both. A QNode is implemented
as a base class to containerize the value and priority and to provide convenient APIs for comparison.

Available methods include:
* insert(item)
* pop()
* peek()

See the doc strings for implementation details.

Instantiation of a PriorityQ takes an iterable which may contain (value, priority) iterables,
non-iterable values, or QNode objects.

##Graph
The graph data class is a network consisting nodes with an arbitrary number of references (edges) to other
nodes in the graph. Methods allows abilities such as adding, removing, and checking the existance of nodes
and edges in the graph. Additionaly, the graph class contains to traversal methods. Given a start node, the
methods will traverse the entire network reachable from that node and return the path travelled as a list of
nodes travelled. Both [depth-first](https://en.wikipedia.org/wiki/Graph_traversal#Depth-first_search) and [breadth first](https://en.wikipedia.org/wiki/Graph_traversal#Breadth-first_search) traversal methods are available.

Available methods include:

* nodes()
* edges()
* add_node(n)
* add_edge(n1, n2)
* del_node(n)
* del_edge(n1, n2)
* has_node(n)
* neighbors(n)
* adjacent(n1, n2)
* depth_first_traversal(start)
* breadth_first_traversal(start)
* uniform_cost_search(n1, n2)
* bellmanford(n1, n2)

The uniform_cost_search method returns a path that corresponds to the
shortest path between n1 and n2. This algorithm tracks historical paths
and is able to search for the shortest path in a relatively uncostly way.
Time complexity is O(edges + node log nodes) with relatively low memory
overhead.

The bellmanfor search method also returns the same path, but has the added
ability to handle edges with negative values and detect negative feedback
loops. It is relatively robust, but at added time complexity cost of
O(nodes * edges).

See the doc strings for additional implementation details.

## BST -- Binary Search Tree
This is a linked-list like tree structure. The Node class implementation
includes a bi-directional relationship between parent and child nodes; the
BST itself naively has knowledge of only the root node directly. The depth, balance and traversal methods traverse the entire tree and therefore have
O(n) time complexity. Insert() and contains() leverage tree sorting to
execute with O(log n) time complexity.

Available methods include:
* insert(val)     --> None
* size()          --> Integer
* contains(val)   --> Boolean
* balance()       --> Integer
* depth()         --> Integer
* in_order()      --> Generator
* pre_order()     --> Generator
* post_order()    --> Generator
* breadth_first() --> Generator
* delete(val)     --> None

See the doc strings for additional implementation details.

[![Build Status](https://travis-ci.org/tpeek/data-structures-1.svg?branch=master)](https://travis-ci.org/tpeek/data-structures-1)
