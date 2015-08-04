def mersort(unslist):
    """Return a sorted list from a list.

    Implementation after psuedocode here:
    https://en.wikipedia.org/wiki/Merge_sort
    """
    if len(unslist) <= 1:
        return unslist
    lunslist = unslist[:len(unslist)/2]
    runslist = unslist[len(unslist)/2:]

    # Recursive calls
    lunslist = mersort(lunslist)
    runslist = mersort(runslist)

    return _merge(lunslist, runslist)


def _merge(llist, rlist):
    """Desructively return an ascending sorted list from two ascending
    sorted lists.

    Implementation after psuedocode here:
    https://en.wikipedia.org/wiki/Merge_sort
    """
    mlist = []
    llist.reverse()
    rlist.reverse()
    while llist and rlist:
        if llist[-1] <= rlist[-1]:
            mlist.append(llist.pop())
        else:
            mlist.append(rlist.pop())
    # For straglers, the following two blocks
    while llist:
        mlist.append(llist.pop())
    while rlist:
        mlist.append(rlist.pop())
    return mlist
