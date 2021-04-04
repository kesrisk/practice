

def printSubset(subset, i, inititalSet):

    if len(inititalSet) == i:
        print(subset)
        return

    printSubset(subset, i+1, inititalSet)
    printSubset(subset + [inititalSet[i]], i+1, inititalSet)


def allSubset(inititalSet):

    printSubset([], 0, inititalSet)



allSubset([1,2,3,4,5,6])