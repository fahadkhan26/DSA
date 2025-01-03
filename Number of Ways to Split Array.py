nums = [10,4,-8,7]

def waysToSplit(nums):
    prefix_sum = [0]
    for i in range(len(nums)):
        prefix_sum.append(nums[i] + prefix_sum[-1])

    count = 0
    for i in range(1, len(prefix_sum)-1):
        if prefix_sum[i] >= prefix_sum[-1] - prefix_sum[i]:
            count += 1
    
    return count