# https://cses.fi/problemset/task/1090


def findNumberOfAgoda(arr, n, x):

    arr = sorted(arr)

    i = 0
    j = n-1
    count = 0

    while j >= i:
        if i == j:
            count += 1
            i += 1
            j -= 1
            continue

        if arr[i] + arr[j] <= x:
            count += 1
            i += 1
            j -= 1
            continue

        count += 1
        j -= 1

    return count


n, x = map(int, input("").split())
arr = list(map(int, input("").split()))
print(findNumberOfAgoda(arr, n, x))