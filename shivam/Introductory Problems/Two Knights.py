# https://cses.fi/problemset/task/1072
# def fact(n):
#
#     if n in factorialDict.keys():
#         return factorialDict[n]
#
#     res = 1
#     for i in range(2, n + 1):
#         res = res * i
#
#     factorialDict[n] = res
#
#     return res

def calculateTotalCombinitionsPossible(totalPositions):
    if totalPositions < 2:
        return 0
    return (totalPositions * (totalPositions - 1))//2

def calculateAttackingPositions(boardDimensions, smallerBoardDimesnsionsAttackingPosition):

    if boardDimensions == 3:
        return 8

    if boardDimensions == 4:
        return 16 + smallerBoardDimesnsionsAttackingPosition

    return ((boardDimensions - 5)*2 + 2 + 3 + 3 + 2 + 2) * 2 + smallerBoardDimesnsionsAttackingPosition

    # return (boardDimensions - 4)*4*2 + 2 + 3 + 3 + 2 + 2 + 2 + 2 + smallerBoardDimesnsionsAttackingPosition


    # we are considering 1st column and last row as outer/outside
    # attackingPositions = 0
    # for boardPosition in range(1, boardDimensions):
    #     if boardPosition + 2 < boardDimensions:
    #         # inside
    #         attackingPositions += 2
    #     if boardPosition + 2 == boardDimensions:
    #         # outside
    #         attackingPositions += 1
    #
    #     if boardPosition - 2 >= 1:
    #         # always inside
    #         attackingPositions += 2
    #
    #     if boardPosition - 1 >= 1:
    #         # always inside
    #         attackingPositions += 2
    #
    #     if boardPosition + 1 < boardDimensions:
    #         # inside
    #         attackingPositions += 2
    #
    #     if boardPosition + 1 == boardDimensions:
    #         # outside
    #         attackingPositions += 1
    #
    # return (attackingPositions//2 * 2 + 2) + smallerBoardDimesnsionsAttackingPosition



def calculateSafePositions(boardDimensions, totalAttackingPositionCountArray):
    if boardDimensions <= 2:
        attackingPostion = 0
    else:
        attackingPostion = calculateAttackingPositions(boardDimensions, totalAttackingPositionCountArray[-1])

    totalAttackingPositionCountArray.append(attackingPostion)
    return calculateTotalCombinitionsPossible(boardDimensions*boardDimensions) - attackingPostion


n = int(input())
# factorialDict = {}
totalAttackingPositionCountArray = []
for i in range(1, n+1):
    print(calculateSafePositions(i, totalAttackingPositionCountArray))