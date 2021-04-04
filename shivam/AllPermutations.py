

def findPermutation(i, subset):

    if i == len(subset) - 1:
        print(subset)

    j = i

    while j < len(subset):
        # replace
        subset[i], subset[j] = subset[j], subset[i]
        findPermutation (i+1, subset)
        j += 1


def allPermutations(initialSet):

    findPermutation(0, initialSet)


allPermutations([1,2,3,4,5])