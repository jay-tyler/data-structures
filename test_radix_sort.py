from radix_sort import radsort
from random import shuffle
import pytest


def test_rand_radixsort():
    tlist = range(500)
    shuffle(tlist)
    tlist = radsort(tlist)
    assert tlist == range(500)


def test_backward_radixsort():
    tlist = range(500)
    tlist.reverse()
    tlist = radsort(tlist)
    assert tlist == range(500)


def test_inorder_radixsort():
    tlist = range(500)
    tlist = radsort(tlist)
    assert tlist == range(500)


def test_sameval_radixsort():
    tlist = [3 for _ in range(500)]
    tlist = radsort(tlist)
    for item in tlist:
        assert item == 3


def test_char_radixsort():
    initlist = list('abcdefghijklmnopq')
    tlist = initlist[:]
    shuffle(tlist)
    tlist = radsort(tlist)
    assert tlist == initlist


def test_bad_case():
    initlist = [10**x for x in range(1000)]
    tlist = list(reversed(initlist))
    tlist = radsort(tlist)
    assert tlist == initlist


def test_oneitemlist_radixsort():
    tlist = [1]
    radsort(tlist)
    assert tlist == [1]


def test_none_radixsort():
    with pytest.raises(TypeError):
        radsort(None)


def test_int_radixsort():
    with pytest.raises(TypeError):
        radsort(1)


def test_str_radixsort():
    with pytest.raises(TypeError):
        radsort("Test.")


def test_dict_radixsort():
    with pytest.raises(TypeError):
        radsort({'a_good_test_dictionary_key': 'a_good_test_dictionary_value'})
