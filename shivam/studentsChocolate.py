

def minChocolateCountDifference(studentsCount, chocolatesArray):

    chocolatesArray = sorted(chocolatesArray)

    chocolatesArrayLenght = len(chocolatesArray)

    maxToMinChocolateDifference = 99999999999

    chocolateIndex = 0

    while chocolateIndex < chocolatesArrayLenght and chocolateIndex + studentsCount -1 < chocolatesArrayLenght:

        currentDifference = chocolatesArray[chocolateIndex + studentsCount -1] - chocolatesArray[chocolateIndex]

        if maxToMinChocolateDifference > currentDifference:
            maxToMinChocolateDifference = currentDifference

        chocolateIndex += 1

    return maxToMinChocolateDifference


studentsCount = int(input())
chocolatesArray = list(map(int, input().split()))
print(minChocolateCountDifference(studentsCount, chocolatesArray))



