
def numberAtPositionXY(y, x):

    if y >= x:

        if y%2 == 1:
            return y*y - (x - 1)
        else:
            return (y-1)*(y-1) + x

    else:
        difference = x - y

        if x%2 == 1:
            return x*x - (x - 1) - difference
        else:
            return (x-1)*(x-1) + x + difference


testcases = int(input())
for _ in range(testcases):

    x, y = map(int, input().split())
    print(numberAtPositionXY(y, x))