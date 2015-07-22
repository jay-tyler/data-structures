import pytest
from bst import BST


def test_find():
    assert BST()._find(42) is None
    aBST = BST(20)
    assert aBST._find(5) == aBST.root
    assert aBST._find(101) == aBST.root


def test_insert():
    aBST = BST()
    aBST.insert(4)
    aBST.insert(2)
    aBST.insert(6)
    aBST.insert(1)
    aBST.insert(3)
    aBST.insert(5)
    aBST.insert(7)
    assert aBST.root.val == 4
    assert aBST.root.parent is None
    assert aBST.root.left.val == 2
    assert aBST.root.left.parent == aBST.root
    assert aBST.root.right.val == 6
    assert aBST.root.right.parent == aBST.root
    assert aBST.root.left.left.val == 1
    assert aBST.root.left.left.parent == aBST.root.left
    assert aBST.root.left.right.val == 3
    assert aBST.root.left.right.parent == aBST.root.left
    assert aBST.root.right.left.val == 5
    assert aBST.root.right.left.parent == aBST.root.right
    assert aBST.root.right.right.val == 7
    assert aBST.root.right.right.parent == aBST.root.right


def test_val_exists():
    aBST = BST()
    aBST.insert(1)
    aBST.insert(1)
    assert aBST.root.left is None
    assert aBST.root.right is None


def test_repr():
    aBST = BST()
    aBST.insert(4)
    aBST.insert(2)
    aBST.insert(6)
    print aBST.root.__repr__()
