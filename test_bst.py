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
    a._size = 6
    return a


@pytest.fixture
def uneven_tree():
    A = Node(6)
    a = BST()
    a.root = A
    A.left = 4
    A.right = 7
    A.left.left = 3
    A.left.right = 5
    A.right.right = 8
    A.right.right.right = 9
    A.right.right.right.right = 10
    a._size = 6
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
    r = aBST.root
    nodes = [r, r.left, r.right, r.left.left, r.left.right, r.right.left,
             r.right.right]
    parent_vals = [None, 4, 4, 2, 2, 6, 6]
    left_child_vals = [2, 1, 5, None, None, None, None]
    right_child_vals = [6, 3, 7, None, None, None, None]
    for node, self_val, p_val, lc_val, rc_val in zip(nodes, nums,
                                                     parent_vals,
                                                     left_child_vals,
                                                     right_child_vals):
        assert node.val == self_val
        if node.parent is not None:
            assert node.parent.val == p_val
        if node.left is not None:
            assert node.left.val == lc_val
        if node.right is not None:
            assert node.right.val == rc_val


def test_val_exists(filled_tree):
    for num in [3, 4, 5, 6, 7, 8]:
        filled_tree.insert(num)
        assert filled_tree.size == 6


def test_size():
    aBST = BST()
    assert aBST.size == 0
    for num, size in zip([6, 2, 8, 4, 1000, -111],
                         [1, 2, 3, 4, 5, 6]):
        aBST.insert(num)
        assert aBST.size == size
    for x in range(2000):
        aBST.insert(uuid4())
    assert aBST.size == 2006


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
    for num, level in zip([4, 2, 6, 1, 3, 5, 7],
                          [(0, 0), (1, 0), (1, 1),
                          (2, 1), (2, 1), (2, 2), (2, 2)]):
        aBST.insert(num)
        assert aBST._lr_levels() == level
    aBST = BST()
    for x in range(20):
        aBST.insert(x)
    assert aBST._lr_levels() == (0, 19)


def test_depth():
    aBST = BST()
    assert aBST.depth() == 0
    for num, depth in zip([4, 2, 6, 3, 7, 8, 9, 10, 11],
                          [1, 2, 2, 3, 3, 4, 5,  6,  7]):
        aBST.insert(num)
        assert aBST.depth() == depth


def test_contains(filled_tree):
    t, f = True, False
    for num, valid in zip([6, 4, 7, 3, 5, 8, 0, 12, 7.5, 2],
                          [t, t, t, t, t, t, f,  f,   f, f]):
        assert filled_tree.contains(num) is valid


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


def test_del_node_with_two_children(filled_tree):
    assert filled_tree.contains(6) is True
    filled_tree.delete(6)
    assert filled_tree.contains(6) is False


def test_del_node_with_one_child(uneven_tree):
    assert uneven_tree.contains(8) is True
    filled_tree.delete(8)
    assert uneven_tree.contains(8) is False


def test_del_node_with_no_children(filled_tree):
    assert filled_tree.contains(8) is True
    filled_tree.delete(8)
    assert filled_tree.contains(8) is False

def test_del_all(filled_tree, uneven_tree):
    for num in [3, 4, 5, 6, 7, 8]:
        filled_tree.delete(num)
        assert filled_tree.contains(num) is False
    for num in [3, 4, 5, 6, 7, 8, 9, 10]:
        uneven_tree.delete(num)
        assert uneven_tree.contains(num) is False
