from dtypes.hash_table import Hash_Table
import pytest


def test_correct_size():
    ht = Hash_Table(100)
    assert ht.num_bins == 100
    assert len(ht.table) == 100


def test_get():
    """Get only accepts Strings or lists of chars.
    Raises an error for all other types."""
    ht = Hash_Table(100)
    for aType in [None, 1, [2, 3], {4: 5}, (6, 7), ht]:
        with pytest.raises(TypeError) as error_info:
            ht.get(aType)


def test_set():
    """Set only accepts Strings or lists of chars.
    Raises an error for all other types."""
    ht = Hash_Table(100)
    for aType in [None, 1, [2, 3], {4: 5}, (6, 7), ht]:
        with pytest.raises(TypeError) as error_info:
            ht.set(aType, "regardless...")


def test_hash():
    """Test hash by placing all entries in system dict to hash and 
    subsequently retrieving"""

    ht = Hash_Table(100000)
    with open('/usr/share/dict/words', 'r') as file:
        lines = file.readlines()
    lines = [line.rstrip('\n') for line in lines]

    for line in lines:
        ht.set(line, line)

    for line in lines:
        testval = ht.get(line)
        assert testval == line
