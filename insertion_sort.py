def insort(unlist):
    """Insertion sort a list

    Implementation follows after gif here
    https://en.wikipedia.org/wiki/Insertion_sort"""
    slist = unlist[:]
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
