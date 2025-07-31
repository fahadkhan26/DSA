# nums = [1,0,1,0,1]
# goal = 2

# def Solution(nums, goal):
#     r = 0
#     l = 0
#     count = 0
#     currSum = nums[r]

#     while r < len(nums):
#         # currSum += nums[r]
#         print(currSum , r, l)
#         if currSum == goal:
#             count += 1
#             print("Count:", count)
#             r += 1
#             currSum += nums[r]

#         elif currSum < goal:
#             r += 1
#             currSum += nums[r]

#         elif currSum >= goal and l < r:
#             # print("in")
#             currSum -= nums[l]
#             l += 1
            

#     return count, currSum


# print(Solution(nums, goal))




# nums = [1,0,1,0,1]
# goal = 2

# def Solution(nums, goal):
#     r = 0
#     l = 0
#     count = 0
#     currSum = nums[r]
#     rightExhaust = False

#     while l <= r:
#         print("r:", r)
#         if r == len(nums) - 1:
#             print("RightE6")
#             rightExhaust == True
        
#         if rightExhaust == False:
#             if currSum == goal:
#                 count += 1
#                 r += 1
#             elif currSum < goal:
#                 r += 1
#             elif currSum >= goal:
#                 currSum -= nums[l]
#                 l += 1
        
#         if rightExhaust == True:
            
#             break
            
#     return count, currSum

# print(Solution(nums, goal))




# nums = [1,0,1,0,1]
# goal = 2

# def BinSubarraysWithSum(nums, goal):
#     l = 0
#     r = 1
#     count = 0
#     currSum = nums[l] + nums[r]

#     while r < len(nums) and l < r:
#         print("l:", l , "  r:", r)
#         if currSum == goal:
#             # print("w")
#             count += 1

#             r += 1
#             currSum += nums[r]

#         elif currSum < goal:
#             r += 1
#             currSum += nums[r]

#         elif currSum > goal:
#             currSum -= nums[l]
#             l += 1
            
#     return count, currSum

# print(BinSubarraysWithSum(nums, goal))



# nums = [1,0,1,0,1]
# goal = 2

# def BinSubarraysWithSum(nums, goal):
#     l = 0
#     count = 0
#     currSum = 0

#     for r in range(len(nums)):
#         currSum += nums[r]
        
        
        
#         # elif currSum < goal:
#         #     currSum += nums[r]


#         while currSum > goal:
#             currSum -=nums[l]
#             l += 1

#         if currSum == goal:
#             count += 1
            
#     return count, currSum

# print(BinSubarraysWithSum(nums, goal))





# nums = [1,0,1,0,1]
# goal = 2

# def BinSubarraysWithSum(nums, goal):
#     l = 0
#     count = 0
#     currSum = 0

#     for r in range(len(nums)):
#         currSum += nums[r]

#         if currSum <= goal:
#             count += 1

            
#     return count, currSum

# print(BinSubarraysWithSum(nums, goal))


nums = [1,0,0,1,1,0]
goal = 2

def BinSubarraysWithSum(nums, goal):
    if goal < 0:
        return 0
    
    l = 0
    currSum = 0
    count = 0

    for r in range(len(nums)):
        currSum += nums[r]

        while currSum > goal:
            currSum -= nums[l]
            l += 1

        if currSum == goal:
            count += 1
        
    return count

print(BinSubarraysWithSum(nums, goal))