def quisort(uslist, lo, hi):
    if lo < hi:
        p = partition(uslist, lo, hi)
        quisort(uslist, lo, p - 1)
        quisort(uslist, p + 1, hi)


def partition(uslist, lo, hi):
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


if __name__ == "__main__":
    """Test time performance for best and worst cases"""
    import time
    from random import shuffle

    # Best case: when the pivot is always the middle value.
    # When the numbers are in random order, the running time
    # will be very close to the best case, nlog(n).
    size = 995
    aList = range(size)
    bList = [1 for _ in range(size)]

    start = time.time()
    for i in range(100):
        shuffle(aList)
        quisort(aList, 0, size - 1)
    stop = time.time()
    best_time = (stop - start)

    # Worst case: When the pivot is always the highest value,
    # or all the values are the same in the list, n^2.
    start = time.time()
    for i in range(100):
        # Keep operations the same for comparison
        shuffle(aList)
        quisort(bList, 0, size - 1)
    stop = time.time()
    worst_time = (stop - start)

    print "Best case is {} times better than worst for n=100\n".format(
        worst_time/best_time)
    print "Best case:  {0:.{1}f} ms\nWorst case: {2:.{3}f} ms".format(
        best_time, 5, worst_time, 5)
