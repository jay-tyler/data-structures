class Hash_Table(object):
    def __init__(self, num_bins):
        self.num_bins = num_bins
        self.table = [[] for x in range(num_bins)]

    def get(self, key):
        """Return the value stored with the given key, if it exists.
        Otherwise, return None."""
        aBin = self.table[self.hash(key)]
        for pair in aBin:
            if pair[0] == key:
                return pair[1]
        return None

    def set(self, key, val):
        """Store the given val using the given key"""
        self.table[self.hash(key)].append([key, val])

    def hash(self, key):
        """Return the hash value of the given key"""
        if type(key) != str:
            raise TypeError('Only keys of type String can be hashed.')
        total = 0
        for char in key:
            total += ord(char)
        return total % self.num_bins
