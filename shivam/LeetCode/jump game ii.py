nums = [2,3,0,1,4]

index = 1

result = [-1 for i in range(len(nums))]

result[0] = 0

while index < len(nums):

    tempIndex = index - 1

    tempArray = []

    while tempIndex >= 0:

        diffOfTempIndexValueAndCurrentIndex = nums[tempIndex] - (index - tempIndex)

        if diffOfTempIndexValueAndCurrentIndex >= 0 and result[tempIndex] != -1:
            tempArray.append(result[tempIndex] + 1)

        tempIndex -= 1
    if len(tempArray) > 0:
        result[index] = min(tempArray)
    index += 1

print(result[-1])