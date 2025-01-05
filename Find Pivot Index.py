def pivotIndex(nums):
    total_sum = sum(nums)
    leftSum = 0
    rightSum = 0

    for i in range(len(nums)):
        rightSum = total_sum - leftSum - nums[i]
        if leftSum == rightSum:
            return i
        else:
            leftSum += nums[i]

    return -1