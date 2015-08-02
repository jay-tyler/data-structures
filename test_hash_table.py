from hash_table import Hash_Table
import pytest


def test_correct_size():
    ht = Hash_Table(100)
    assert ht.num_bins == 100
    assert len(ht.table) == 100


def test_get():
    """Get only excepts Strings or lists of chars.
    Raises an error for all other types."""
    ht = Hash_Table(100)
    for aType in [None, 1, [2, 3], {4: 5}, (6, 7), ht]:
        with pytest.raises(TypeError) as error_info:
            ht.get(aType)


def test_set():
    """Set only excepts Strings or lists of chars.
    Raises an error for all other types."""
    ht = Hash_Table(100)
    for aType in [None, 1, [2, 3], {4: 5}, (6, 7), ht]:
        with pytest.raises(TypeError) as error_info:
            ht.set(aType, "regardless...")


def test_hash():
    pass
