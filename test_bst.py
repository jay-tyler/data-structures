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
    assert aBST.root.left.val == 2
    assert aBST.root.right.val == 6
    assert aBST.root.left.left.val == 1
    assert aBST.root.left.right.val == 3
    assert aBST.root.right.left.val == 5
    assert aBST.root.right.right.val == 7


def test_val_exists():
    aBST = BST()
    aBST.insert(1)
    aBST.insert(1)
    assert aBST.root.left is None
    assert aBST.root.right is None
