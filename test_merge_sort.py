from merge_sort import mersort, merge
from random import randint
import pytest


def test_merge():
    aList = [1, 3, 5, 7, 9]
    bList = [0, 2, 4, 6, 8]
    assert merge(aList, bList) == range(1, 11)
