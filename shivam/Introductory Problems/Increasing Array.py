# https://cses.fi/problemset/task/1094

def increasingArray(n, arr):

    count = 0

    for i in range(1, n):
        if arr[i-1] > arr[i]:
            diff = arr[i-1] - arr[i]
            count += diff
            arr[i] += diff

    return count



n = int(input(""))
arr = list(map(int, input("").split()))
print(increasingArray(n, arr))