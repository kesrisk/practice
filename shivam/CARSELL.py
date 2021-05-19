# https://www.codechef.com/APRIL20B/problems/CARSELL

def maxProfit(arr, n):
    profit = 0
    arr = sorted(arr)[::-1]
    for i in range(n):
        temp = arr[i] - i
        if temp < 0:
            temp = 0
        profit += temp

    return profit

cases =  int(input())
for _ in range(cases):
    n = int(input())
    arr = list(map(int, input().split()))
    print(maxProfit(arr, n))