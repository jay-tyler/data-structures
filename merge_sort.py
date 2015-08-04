
def merge(llist, rlist):
    mlist = []
    llist = llist[:]
    rlist = rlist[:]
    llist.reverse()
    rlist.reverse()
    while llist and rlist:
        if llist[-1] <= rlist[-1]:
            mlist.append(llist.pop())
        else:
            mlist.append(rlist.pop())
    #For straglers, the following two blocks
    while llist:
        mlist.append(llist.pop())
    while rlist:
        mlist.append(rlist.pop())
    return mlist