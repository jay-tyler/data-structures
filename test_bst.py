import pytest
from bst import BST, Node
from uuid import uuid4


@pytest.fixture
def filled_tree():
    A = Node(6)
    a = BST()
    a.root = A
    A.left = 4
    A.right = 7
    A.left.left = 3
    A.left.right = 5
    A.right.right = 8
    return a


def test_find():
    assert BST()._find(42) is None
    aBST = BST(20)
    assert aBST._find(5) == aBST.root
    assert aBST._find(101) == aBST.root


def test_insert():
    aBST = BST()
    nums = [4, 2, 6, 1, 3, 5, 7]
    for num in nums:
        aBST.insert(num)
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
    aBST.insert(2)
    aBST.insert(2)
    assert aBST.root.left is None
    assert aBST.root.right is None
    assert aBST.size == 1
    aBST.insert(1)
    aBST.insert(3)
    aBST.insert(1)
    aBST.insert(3)
    assert aBST.size == 3


def test_size():
    aBST = BST()
    assert aBST.size == 0
    aBST.insert("Jason")
    assert aBST.size == 1
    aBST.insert("Tyler")
    assert aBST.size == 2
    aBST.insert("I cant use Tyler again")
    assert aBST.size == 3
    aBST.insert("Peek")
    assert aBST.size == 4
    for x in range(2000):
        aBST.insert(uuid4())
    assert aBST.size == 2004


def test_balance():
    aBST = BST()
    assert aBST.balance() == 0
    for num, bal in zip([4, 2, 6, 3, 7, 8, 9, 10, 11],
                        [0, 1, 0, 1, 0, -1, -2, -3]):
        aBST.insert(num)
        assert aBST.balance() == bal


def test_lr_levels():
    aBST = BST()
    assert aBST._lr_levels() == None
    aBST.insert(4)
    assert aBST._lr_levels() == (0, 0)
    aBST.insert(2)
    aBST.insert(6)
    aBST.insert(1)
    aBST.insert(3)
    aBST.insert(5)
    aBST.insert(7)
    assert aBST._lr_levels() == (2, 2)
    aBST = BST()
    for x in range(20):
        aBST.insert(x)
    assert aBST._lr_levels() == (0, 19)


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


def test_pre_order(filled_tree):
    assert list(BST().pre_order()) == []
    assert list(BST(1).pre_order()) == [1]
    assert list(filled_tree.pre_order()) == [6, 4, 3, 5, 7, 8]


def test_in_order(filled_tree):
    assert list(BST().in_order()) == []
    assert list(BST(1).in_order()) == [1]
    assert list(filled_tree.in_order()) == [3, 4, 5, 6, 7, 8]


def test_post_order(filled_tree):
    assert list(BST().post_order()) == []
    assert list(BST(1).post_order()) == [1]
    assert list(filled_tree.post_order()) == [3, 5, 4, 8, 7, 6]


def test_breadth_first(filled_tree):
    assert list(BST().breadth_first()) == []
    assert list(BST(1).breadth_first()) == [1]
    assert list(filled_tree.breadth_first()) == [6, 4, 7, 3, 5, 8]
