def maxPoints(arr, n):
    if n == len(arr):
        return sum(arr)
    elif n == 1:
        return max(arr[0], arr[-1])
    
    l = -n
    r = -1
    maxSum = sum(arr[l:r] + [arr[-1]])
    tempSum = maxSum
    while r < n - 1:
        tempSum -= arr[l]
        l += 1
        r += 1
        tempSum += arr[r]
        maxSum = max(maxSum, tempSum)
    
    return maxSum