

intervals = [[1,3],[2,6],[8,10],[15,18]]
result = []

tempArray = []
mainIndex = 0

while mainIndex < len(intervals):


    if len(tempArray) == 0:
        tempArray.append(intervals[mainIndex][0])
        continue

    if mainIndex + 1 < len(intervals):
        altIndex = mainIndex + 1

        while (altIndex < len(intervals)):
            if intervals[mainIndex][1] > intervals[altIndex][0] and intervals[mainIndex][1] > intervals[altIndex][1]:
                altIndex += 1
                continue
            if intervals[mainIndex][1] >= intervals[altIndex][0]:
                tempArray.append(intervals[altIndex][1])
                result.append(tempArray)
                tempArray = []
                mainIndex = altIndex + 1
                break

            tempArray.append(intervals[mainIndex][1])
            result.append(tempArray)
            tempArray = []
            mainIndex = altIndex
            break


        if altIndex > len(intervals):
            tempArray.append(intervals[altIndex - 1][1])
            result.append(tempArray)
            tempArray = []
            break


    else:
        if (len(tempArray) == 1):
            tempArray.append(intervals[mainIndex][1])
            result.append(tempArray)
        break



print(result)