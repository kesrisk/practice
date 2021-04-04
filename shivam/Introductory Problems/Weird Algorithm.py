# https://cses.fi/problemset/task/1068


def operationforOdd(n):
    print(n * 3 + 1, end=" ")
    return n * 3 + 1

def operationForEven(n):
    print(n//2, end=" ")
    return n//2

def weirdAlgo(n):

    if n == 1:
        return n

    if n % 2 == 0:
        return weirdAlgo(operationForEven(n))

    return weirdAlgo(operationforOdd(n))




n = int(input())

print(n, end=" ")
weirdAlgo(n)