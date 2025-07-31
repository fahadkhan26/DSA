#Constant Window

arr = [-1,2,3,3,4,5,-1]
k = 4

#Max sum of 4 consecutive elements

def maxSum(arr, k):
    l = arr[0]
    r = arr[k-1]
    maxConsSum = 0
    currSum = 0

    i = 0
    while i <= r:
        currSum += arr[i]

