class Solution:
    def findMaxAverage(self, nums, k: int) -> float:
        l = 0
        r = k-1

        winSum = sum(nums[:r+1])
        maxSum = winSum

        while r < len(nums)-1:
            winSum -= nums[l]
            l += 1
            r += 1
            winSum += nums[r]

            maxSum = max(winSum, maxSum)

        return maxSum/k