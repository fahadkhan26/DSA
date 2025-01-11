def maxConOnes(nums, k):
    maxlen = 0
    l = 0
    r = 0
    zeros = 0

    for r in range(len(nums)):
        if nums[r] == 0:
            zeros += 1
        while zeros > k:
            if nums[l] == 0:
                zeros -= 1
            l += 1
        maxlen = max(maxlen, r - l + 1)
    return maxlen