def searchInsert(nums, target):
    low = 0
    high = len(nums) - 1
    while True:
        if low > high:
            return high+1
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1