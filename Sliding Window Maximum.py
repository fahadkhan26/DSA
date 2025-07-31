nums = [1,3,-1,-3,5,3,6,7]
k = 3

def slideMax(nums, k):
    maxNums = []
    l = 0
    r = k - 1

    while r < len(nums):
        maxNums.append(max(nums[l:r+1]))
        l += 1
        r += 1
    return maxNums



print(slideMax(nums, k))