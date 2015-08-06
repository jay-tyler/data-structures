if __name__ == "__main__":
    """Test time performance for best and worst cases"""
    import time

    size = 1000

    # Best case: when all numbers in the list have the same number of digits.
    good_list = range(size + 1)
    start = time.time()
    for i in range(100):
        radsort(good_list)
    stop = time.time()
    best_time = (stop - start)

    # Worst case: When there is one very large outlier.
    bad_list = [1 for _ in range(size)] + [10**10]
    start = time.time()
    for i in range(100):
        radsort(bad_list)
    stop = time.time()
    worst_time = (stop - start)

    print "Best case is {} times better than worst for n=100\n".format(
        worst_time/best_time)
    print "Best case:  {0:.{1}f} ms\nWorst case: {2:.{3}f} ms".format(
        best_time, 5, worst_time, 5)
