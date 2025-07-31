# s = "bbcbaba"

# def unique(s):
#     left = 0
#     right = len(s) - 1

#     while right >= left:
#         if s[right] != s[left]:
#             right -= 1
#         else:
#             break
    
#     if right == left:
#         return 0
    
#     non_used = ""
#     count = 0
#     for i in range(1, right+1):
#         if s[i] not in non_used:
#             non_used += s[i]
#             count += 1

#     print(left, right)
#     print(non_used, count)

# print(unique(s))





s = "abca"

def unique(s):

    middle = 1
    unique_set = set()

    while middle < len(s) - 1:
        left = set(s[:middle])
        right = set(s[middle + 1 :])
        # print(right)

        for char in left:
            if char in right:
                unique_set.add(char + s[middle] + char)
        middle += 1
    
    return len(unique_set)
print(unique(s))