# https://cses.fi/problemset/task/1091

def ticket(ticketArr, custArr):

    ticketArr = sorted(ticketArr)[::-1]

    for cust in custArray:

        # prev = 0
        next = 0

        while next < len(ticketArr):

            if cust >= ticketArr[next]:
                print(ticketArr[next])
                ticketArr.remove(ticketArr[next])
                break

        print(-1)

n, m = map(int, input().split())
ticketArray = list(map(int, input().split()))
custArray = list(map(int, input().split()))
ticket(ticketArray, custArray)
