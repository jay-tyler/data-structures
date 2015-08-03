def insort(slist):
    """Insertion sort a list

    Implementation follows after gif here
    https://en.wikipedia.org/wiki/Insertion_sort"""

    for i in range(1, len(slist)):
        j = i - 1
        while j >= 0:
            if slist[i] < slist[j]:
                slist[i], slist[j] = slist[j], slist[i]
                j -= 1
                i -= 1
            else:
                break 
    return slist


if __name__ == "__main__":
    """Test time performance for best and worst cases"""
    import time
    # time is better than timeit for unix times
    # https://docs.python.org/2/library/timeit.html#timeit.default_timer

    # O(n) best case
    start = time.time()
    for i in range(100):
        insort(range(100))
    stop = time.time()
    best_time = (stop - start) / 100

    # O(n**2) worst case 
    start = time.time()
    for i in range(100):
        insort(range(100)[::-1])
    stop = time.time()
    worst_time = (stop - start) / 100

    print "Best case is {:.1f} times better than worst for n=100\n\n".format(
        worst_time/best_time) +\
        "best case: {best:.2E} s\n\nworst case: {worst:.2E} s".format(
        best=best_time, worst=worst_time)
