def quisort(uslist, lo=None, hi=None):
    """Sort in-place an unsorted list or slice of a list

    lo and hi correspond to the start and stop indices for the list slice"""

    if hi is None:
        hi = len(uslist) - 1
    if lo is None:
        lo = 0

    def partition(uslist, lo, hi):
        """Compare and swap values over list slice"""
        p = uslist[hi]
        i = lo - 1
        j = lo
        while j < hi:
            if uslist[j] <= p:
                i = i + 1
                uslist[i], uslist[j] = uslist[j], uslist[i]
            j += 1
        i += 1
        uslist[i], uslist[hi] = uslist[hi], uslist[i]
        return i

    if lo < hi:
        p = partition(uslist, lo, hi)
        quisort(uslist, lo, p - 1)
        quisort(uslist, p + 1, hi)


if __name__ == "__main__":
    """Test time performance for best and worst cases"""
    import time
    from random import shuffle

    # Best case: when the pivot is always the middle value.
    # When the numbers are in random order, the running time
    # will be very close to the best case, nlog(n).
    size = 995
    a_list = range(size)
    b_list = [1 for _ in range(size)]

    start = time.time()
    for i in range(100):
        shuffle(a_list)
        quisort(a_list)
    stop = time.time()
    best_time = (stop - start)

    # Worst case: When the pivot is always the highest value,
    # or all the values are the same in the list, n^2.
    start = time.time()
    for i in range(100):
        # Keep operations the same for comparison
        shuffle(a_list)
        quisort(b_list)
    stop = time.time()
    worst_time = (stop - start)

    print "Best case is {} times better than worst for n=100\n".format(
        worst_time/best_time)
    print "Best case:  {0:.{1}f} ms\nWorst case: {2:.{3}f} ms".format(
        best_time, 5, worst_time, 5)
