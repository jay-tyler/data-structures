from insertion_sort import insort
from random import randint
import pytest


def test_insertion_sort_best():
    n = 1000000
    aList = range(n)
    assert insort(aList) == range(n)


def test_insertion_sort_worst():
    n = 1000
    aList = range(n)[::-1]
    assert insort(aList) == range(n)
    assert aList != range(n)
    assert aList == range(n)[::-1]


def test_insertion_sort_random():
    n = 1000
    random_list = [randint(1, n) for _ in range(n)]
    sorted_list = sorted(random_list)
    assert random_list != sorted_list
    assert insort(random_list) == sorted_list


def test_insertion_sort_fail():
    for item in [1, None, (2, 1), {'1': 1, '2': 2}]:
        with pytest.raises(TypeError):
            insort(item)
    with pytest.raises(TypeError):
        insort()
