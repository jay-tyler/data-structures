from __future__ import unicode_literals
import pytest
import dtypes.linked_list as ll

#######################################################################
# Fixtures and testing constants
#######################################################################


@pytest.fixture
def base_llist():
    return ll.LinkedList([1, 2, 3])


@pytest.fixture
def second_llist():
    return ll.LinkedList([4, 5, 6])

#######################################################################
# Instantiation testing
#######################################################################


def test_construct_from_iterable_valid(base_llist):
    expected_output = "(1, 2, 3)"
    assert base_llist.display() == expected_output


def test_construct_from_nested_iterable_valid():
    arg = ([1, 2, 3], 'string')
    expected_output = "([1, 2, 3], u'string')"
    assert ll.LinkedList(arg).__str__() == expected_output


def test_construct_from_string_valid():
    arg = "string"
    expected_output = "(u's', u't', u'r', u'i', u'n', u'g')"
    assert ll.LinkedList(arg).__str__() == expected_output


def test_construct_empty_valid():
    expected_output = "()"
    assert ll.LinkedList().__str__() == expected_output


def test_construct_from_none_fails():
    with pytest.raises(TypeError):
        ll.LinkedList(None)


def test_construct_from_single_integer_fails():
    with pytest.raises(TypeError):
        ll.LinkedList(2)


#######################################################################
# Tests for special, non-list() like functions
#######################################################################
# TODO: Reorganize what's here.

def test_insert_single_value(base_llist):
    base_llist.insert(4)
    assert base_llist.__str__() == "(4, 1, 2, 3)"


def test_pop(base_llist):
    assert base_llist.pop() == 1
    assert base_llist.__str__() == "(2, 3)"


def test_size(base_llist):
    assert base_llist.size() == 3


def test_search_val(base_llist):
    searched_node = base_llist.search(2)
    assert isinstance(searched_node, ll.Node)
    assert searched_node.val == 2


def test_remove_node(base_llist):
    base_llist.remove(base_llist.search(2))
    assert base_llist.__str__() == "(1, 3)"


def test_display(base_llist):
    assert base_llist.display() == "(1, 2, 3)"


#######################################################################
# Tests for list() like functions
#######################################################################
def _getvals(llist_in):
    """Test helper to get LinkedList vals independent of any class functions"""
    node = llist_in.head
    vals = []
    while True:
        vals.append(node.val)
        node = node.next
        if node is None:
            break
    return vals


def test_dunder_add(base_llist, second_llist):
    new_llist = base_llist + second_llist
    assert _getvals(new_llist) == _getvals(base_llist) + _getvals(second_llist)


def test_dunder_iadd(base_llist, second_llist):
    prev_vals = _getvals(base_llist)
    base_llist += second_llist
    assert _getvals(base_llist) == prev_vals + _getvals(second_llist)


def test_append(base_llist):
    prev_vals = _getvals(base_llist) # Returns Python list
    base_llist.append(5)
    prev_vals.append(5)
    assert _getvals(base_llist) == prev_vals