# https://cses.fi/problemset/task/1091
# [4,3,4] => [3,-1,0]
def ticket(ticketArr, custArr):

    ticketDIct = {}

    for i in custArr:
        ticketDIct[i] = None

    # decreasing array
    ticketArr = sorted(ticketArr)[::-1]
    custArr = sorted(custArr)[::-1]


    custIndex = 0
    ticketIndex = 0

    while custIndex < len(custArr):

        ticketAssigned: bool = False

        while ticketIndex < len(ticketArr):

            if ticketArr[ticketIndex] <= custArr[custIndex]:
                ticketDIct[custArr[custIndex]] = ticketArr[ticketIndex]
                ticketIndex += 1
                custIndex += 1
                ticketAssigned = True
                break

            ticketIndex += 1

        if not ticketAssigned:
            ticketDIct[custArr[custIndex]] = -1
            custIndex += 1

    return ticketDIct.values()


n, m = map(int, input().split())
ticketArray = list(map(int, input().split()))
custArray = list(map(int, input().split()))
[print(x) for x in ticket(ticketArray, custArray)]
