

def singleOccurance(n , arr):

    result = 0

    for i in arr:
        result = result^i

    return result

n = int(input())
arr = list(map(int, input().split()))

print(singleOccurance(n, arr))