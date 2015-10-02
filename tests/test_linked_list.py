from __future__ import unicode_literals
import pytest
import sys
from dtypes.linked_list import LinkedList, Node


#######################################################################
# Fixtures, helpers, and testing constants
#######################################################################
INSTANTIATION_ARG_1 = [1, 2, 3, 5, 3]
INSTANTIATION_ARG_2 = [4, 5, 6]
INSTANTIATION_ARG_3 = [1]

@pytest.fixture
def first_llist():
    return LinkedList(INSTANTIATION_ARG_1)


@pytest.fixture
def second_llist():
    return LinkedList(INSTANTIATION_ARG_2)


@pytest.fixture
def one_item_llist():
    return LinkedList(INSTANTIATION_ARG_3)


@pytest.fixture
def empty_llist():
    return LinkedList()


def _getvals(llist_in):
    """Return LinkedList vals as list"""
    node = llist_in.head
    vals = []
    while True:
        vals.append(node.val)
        node = node.next
        if node is None:
            break
    return vals


def _makestr(llist_in):
    """Return a string from a list or LinkedList that should be equivalent to LinkedList.__str__()

    e.g.
    >>> a = LinkedList([1,2,3])
    >>> _makestr(a)
    "(1, 2, 3)"
    """
    if isinstance(llist_in, LinkedList):
        return str(tuple(_getvals(llist_in)))
    else:
        return str(tuple(llist_in))


#######################################################################
# Instantiation testing
#######################################################################


def test_construct_from_iterable_valid(first_llist):
    expected_output = _makestr(first_llist)
    assert first_llist.display() == expected_output


def test_construct_from_nested_iterable_valid():
    arg = ([1, 2, 3], 'string')
    expected_output = "([1, 2, 3], u'string')"
    assert LinkedList(arg).__str__() == expected_output


def test_construct_from_string_valid():
    arg = "string"
    expected_output = "(u's', u't', u'r', u'i', u'n', u'g')"
    assert LinkedList(arg).__str__() == expected_output


def test_construct_empty_valid():
    expected_output = "()"
    assert LinkedList().__str__() == expected_output


def test_construct_from_none_fails():
    with pytest.raises(TypeError):
        LinkedList(None)


def test_construct_from_single_integer_fails():
    with pytest.raises(TypeError):
        LinkedList(2)


#######################################################################
# Tests for special, non-list() like functions
#######################################################################
# TODO: Reorganize what's here.


def test_insert_single_value(first_llist):
    as_list = _getvals(first_llist)
    first_llist.insert(4)
    as_list.insert(0, 4)
    assert _getvals(first_llist) == as_list


def test_pop_index_0(first_llist):
    as_list = _getvals(first_llist)
    expected_pop = as_list.pop(0)
    assert first_llist.pop() == expected_pop
    assert first_llist.__str__() == _makestr(as_list)  # This line will break if __str__ spec changes; use testing helpers and replace all instances of this pattern


def test_pop_index_2(first_llist):
    as_list = _getvals(first_llist)
    expected_pop = as_list.pop(2)
    assert first_llist.pop(2) == expected_pop
    assert first_llist.__str__() == _makestr(as_list)


def test_pop_index_last(first_llist):
    length = len(INSTANTIATION_ARG_1)
    as_list = _getvals(first_llist)
    expected_pop = as_list.pop(length - 1)
    assert first_llist.pop(length - 1) == expected_pop
    assert first_llist.__str__() == _makestr(as_list)


def test_pop_index_last_as_alias_minus_one(first_llist):
    as_list = _getvals(first_llist)
    expected_pop = as_list.pop(-1)
    assert first_llist.pop(-1) == expected_pop
    assert first_llist.__str__() == _makestr(as_list)


def test_size_full(first_llist):
    assert first_llist.size() == len(_getvals(first_llist))


def test_size_one(one_item_llist):
    assert one_item_llist.size() == 1


def test_size_empty(empty_llist):
    assert empty_llist.size() == 0


def test_len_full(first_llist):
    assert len(first_llist) == len(_getvals(first_llist))


def test_len_one(one_item_llist):
    assert len(one_item_llist) == 1


def test_len_empty(empty_llist):
    assert len(empty_llist) == 0


def test_search_val(first_llist):
    searched_node = first_llist.search(2)
    assert isinstance(searched_node, Node)
    assert searched_node.val == 2


def test_remove_node(first_llist):
    as_list = _getvals(first_llist)
    as_list.remove(2)
    first_llist.remove(first_llist.search(2))
    assert first_llist.__str__() == str(tuple(as_list))


def test_display(first_llist):
    assert first_llist.display() == _makestr(first_llist)


#######################################################################
# Tests for list() like functions
#######################################################################


def test_dunder_add(first_llist, second_llist):
    new_llist = first_llist + second_llist
    assert _getvals(new_llist) == _getvals(first_llist) + _getvals(second_llist)


def test_dunder_iadd(first_llist, second_llist):
    as_list = _getvals(first_llist)
    first_llist += second_llist
    as_list += _getvals(second_llist)
    assert _getvals(first_llist) == as_list


def test_append(first_llist):
    as_list = _getvals(first_llist)
    first_llist.append(5)
    as_list.append(5)
    assert _getvals(first_llist) == as_list


def test_clear(first_llist):
    # Note that .clear() doesn't appear as a Py list method until Py3.3
    first_llist.clear()
    assert first_llist.head is None


def test_dunder_contains_true(first_llist):
    as_list = _getvals(first_llist)
    expected_val = INSTANTIATION_ARG_1[1]
    assert (expected_val in first_llist) == (expected_val in as_list)
    assert (expected_val in first_llist) is True


def test_dunder_contains_false(first_llist):
    as_list = _getvals(first_llist)
    unexpected_val = sys.maxint
    assert (unexpected_val in first_llist) == (unexpected_val in as_list)
    assert (unexpected_val in first_llist) is False


def test_copy(first_llist):
    as_list = _getvals(first_llist)
    copy_of_llist = first_llist.copy()
    assert id(copy_of_llist) != id(first_llist)
    assert _getvals(copy_of_llist) == as_list
