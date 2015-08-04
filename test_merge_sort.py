from merge_sort import mersort, _merge
from random import randint
import pytest


def test_merge():
    aList = range(1, 11, 2)
    bList = range(0, 10, 2)
    assert _merge(aList, bList) == range(10)


def test_mersort():
    n = 1000
    random_list = [randint(1, n) for _ in range(n)]
    sorted_list = sorted(random_list)
    assert random_list != sorted_list
    assert mersort(random_list) == sorted_list
    assert random_list != sorted_list


def test_mersort_easy():
    n = 10000
    assert mersort(range(n)) == range(n)


def test_mersort_backward():
    n = 10000
    aList = range(n)
    aList.reverse()
    assert mersort(aList) == range(n)


def test_insertion_sort_fail():
    for item in [1, None, {'1': 1, '2': 2}]:
        with pytest.raises(TypeError):
            mersort(item)
    for item in [(2, 1), 'foobar']:
        with pytest.raises(AttributeError):
            mersort(item)
