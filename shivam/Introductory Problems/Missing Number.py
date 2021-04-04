# https://cses.fi/problemset/task/1083

# try to solve using bitwise operator
# recursiveSum is not working as expected
def recursiveSum(a):
    if len(a) == 1:
        return a[0]
    return arr[0] + recursiveSum(a[1:])

def getSumOfNNumbers(n):
    return (n*(n + 1))//2



def findMissing(n, arr):

    # sumOfElementsOfArray = recursiveSum(arr)
    sumOfElementsOfArray = sum(arr)
    sumOfNNumbers = getSumOfNNumbers(n)

    return sumOfNNumbers - sumOfElementsOfArray

def findViaBitWiseOperator(n, arr):

    xorOfArr = 0
    xorOfNNumbers = 0

    for i in range(n+1):
        xorOfNNumbers ^= i

    for i in arr:
        xorOfArr ^= i

    return  xorOfArr ^ xorOfNNumbers



n = int(input(""))
arr = list(map(int, input("").split()))
print(findViaBitWiseOperator(n, arr))