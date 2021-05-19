# https://www.codechef.com/APRIL20B/problems/COVIDLQ


def checkCOVID19Queue(arr, n):
    start = 0
    count = 0

    for i in range(n):
        if arr[i] == 1:
            start = i
            break

    for i in range(start+1, n):
        if arr[i] == 0:
            count += 1
        else:
            if count >= 5:
                # safe
                count = 0
            else:
                return "NO"
    return "YES"


t = int(input())
for _ in range(t):

    n  = int(input())
    arr = list(map(int, input().split()))
    print(checkCOVID19Queue(arr, n))
