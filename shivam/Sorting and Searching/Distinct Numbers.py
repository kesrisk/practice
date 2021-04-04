# https://cses.fi/problemset/task/1621

def distinctNumber(n, arr):

    d = {}

    for i in range(n):
        if arr[i] in d.keys():
            continue
        d[arr[i]] = 1

    return len(d.keys())


n = int(input(""))
arr = list(map(int, input("").split()))
print(distinctNumber(n, arr))