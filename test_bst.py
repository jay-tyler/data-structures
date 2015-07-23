import pytest
from bst import BST, Node
from uuid import uuid4


@pytest.fixture
def filled_tree():
    A = Node(6)
    B = Node(4, parent=A)
    C = Node(7, parent=A)
    D = Node(3, parent=B)
    E = Node(5, parent=B)
    F = Node(8, parent=C)

    # Backrefs
    A.left = B
    A.right = C
    B.left = D
    B.right = E
    C.right = F

    a = BST()
    a.root = A
    return a


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


def test_size():
    aBST = BST()
    assert aBST.size() == 0
    aBST.insert("Jason")
    assert aBST.size() == 1
    aBST.insert("Tyler")
    assert aBST.size() == 2
    aBST.insert("I cant use Tyler again")
    assert aBST.size() == 3
    aBST.insert("Peek")
    assert aBST.size() == 4
    for x in range(2000):
        aBST.insert(uuid4())
    assert aBST.size() == 2004


def test_balance():
    aBST = BST()
    assert aBST.balance() == 0
    aBST.insert(4)
    assert aBST.balance() == 0
    aBST.insert(2)
    assert aBST.balance() == 1
    aBST.insert(6)
    assert aBST.balance() == 0
    aBST.insert(3)
    assert aBST.balance() == 1
    aBST.insert(7)
    assert aBST.balance() == 0
    aBST.insert(8)
    assert aBST.balance() == -1
    aBST.insert(9)
    assert aBST.balance() == -2
    aBST.insert(10)
    assert aBST.balance() == -3
    aBST.insert(11)
    for x in range(2000):
        aBST.insert(uuid4())
    assert aBST.balance != 0


def test_lr_levels():
    aBST = BST()
    assert aBST.lr_levels() == None
    aBST.insert(4)
    assert aBST.lr_levels() == (0, 0)
    aBST.insert(2)
    aBST.insert(6)
    aBST.insert(1)
    aBST.insert(3)
    aBST.insert(5)
    aBST.insert(7)
    assert aBST.lr_levels() == (2, 2)
    aBST = BST()
    for x in range(20):
        aBST.insert(x)
    assert aBST.lr_levels() == (0, 19)


def test_depth():
    aBST = BST()
    assert aBST.depth() == 0
    aBST.insert(4)
    assert aBST.depth() == 1
    aBST.insert(2)
    assert aBST.depth() == 2
    aBST.insert(6)
    assert aBST.depth() == 2
    aBST.insert(3)
    assert aBST.depth() == 3
    aBST.insert(7)
    assert aBST.depth() == 3
    aBST.insert(8)
    assert aBST.depth() == 4
    aBST.insert(9)
    assert aBST.depth() == 5
    aBST.insert(10)
    assert aBST.depth() == 6
    aBST.insert(11)
    assert aBST.depth() == 7


def test_contains(filled_tree):
    assert filled_tree.contains(6) is True
    assert filled_tree.contains(4) is True
    assert filled_tree.contains(7) is True
    assert filled_tree.contains(3) is True
    assert filled_tree.contains(5) is True
    assert filled_tree.contains(8) is True
    assert filled_tree.contains(0) is False
    assert filled_tree.contains(12) is False
    assert filled_tree.contains(7.5) is False
    assert filled_tree.contains(2) is False
