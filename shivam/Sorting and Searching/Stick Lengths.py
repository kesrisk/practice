# https://cses.fi/problemset/task/1074
import math
import statistics


def calculateCost(arr, n):

    medianVal = statistics.median(arr)
    resultFloor = 0
    for i in arr:
        resultFloor += abs(i - medianVal)
    return int (resultFloor)

def newSol(A, n):
    return sum(A[-n:A.sort()]) - sum(A[:n])

n = int(input())
arr = list(map(int, input().split()))
print(newSol(arr, n))
# print(calculateCost(arr, n))