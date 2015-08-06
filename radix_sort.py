

def radsort(unslist):
    # find max for iterative solution
    maxval = max(unslist)
    ntimes = len(str(maxval))

    slist = unslist[:]

    for n in range(ntimes):
        # Making radix bins
        bins = []
        for i in range(10):
            bins.append(list())

        # Place each list item in appropriate bin
        for i, item in enumerate(slist):
            inspecting = slist[i]
            digval = _get_nth_digit(inspecting, n)
            bins[digval].append(inspecting)

        slist = []
        # Flatten bins to list
        for bin in bins:
            for item in bin:
                slist.append(item)

    return slist

def _get_nth_digit(num, n):
    """For a positive integer, get the value at the nth digit;
    indexing starts at 0"""

    return ((num % (10 ** (n + 1))) - (num % (10 ** (n)))) // 10 ** n
