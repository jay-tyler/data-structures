from quick_sort import quisort
from random import shuffle


def test_quicksort():
    aList = range(1000)
    shuffle(aList)
    assert aList != range(1000)
    quisort(aList, 0, len(aList)-1)
    assert aList == range(1000)
