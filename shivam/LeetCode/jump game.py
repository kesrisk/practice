# https://leetcode.com/problems/jump-game/


nums = [3,2,1,0,4]
index = 1
result = [False for i in range(len(nums))]
result[0] = True

while index < len(nums):

    tempIndex = index - 1

    while tempIndex >= 0:

        if result[tempIndex] == False:
            tempIndex -= 1
            continue

        diffOfTempIndexValueAndCurrentIndex = nums[tempIndex] - (index - tempIndex)

        if diffOfTempIndexValueAndCurrentIndex >= 0:
            result[index] = True
            break

        tempIndex -= 1
    index += 1

print(result)