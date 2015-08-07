from quick_sort import quisort
from random import shuffle
import pytest


def test_rand_quicksort():
    tlist = range(500)
    shuffle(tlist)
    assert tlist != range(500)
    quisort(tlist)
    assert tlist == range(500)


def test_backward_quicksort():
    tlist = range(500)
    tlist.reverse()
    quisort(tlist)
    assert tlist == range(500)


def test_inorder_quicksort():
    tlist = range(500)
    quisort(tlist)
    assert tlist == range(500)


def test_sameval_quicksort():
    tlist = [3 for _ in range(500)]
    quisort(tlist)
    for item in tlist:
        assert item == 3


def test_char_quicksort():
    initlist = list('abcdefghijklmnopq')
    tlist = initlist[:]
    shuffle(tlist)
    quisort(tlist)
    assert tlist == initlist


def test_none_quicksort():
    tlist = None
    with pytest.raises(TypeError):
        quisort(tlist)


def test_oneitemlist_quicksort():
    tlist = [1]
    quisort(tlist)
    assert tlist == [1]


def test_oneitem_quicksort():
    tlist = 1
    with pytest.raises(TypeError):
        quisort(tlist)
