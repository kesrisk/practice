# https://cses.fi/problemset/task/1069


def maxSubStringRecursive(s, total, current, currentCount):

    if len(s) == 1:
        return total

    if current == s[0]:
        currentCount += 1
    else:
        currentCount = 1

    if total < currentCount:
        total = currentCount

    return maxSubStringRecursive(s[1:], total, s[0], currentCount)

def maxSubString(s, total, current, currentCount):

    for i in s:
        if current == i:
            currentCount += 1
        else:
            currentCount = 1

        if total < currentCount:
            total = currentCount

        current = i
    return total

inputStr = input()
print(maxSubString(inputStr, 0, '', 0))