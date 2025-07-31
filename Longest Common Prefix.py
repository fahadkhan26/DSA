strs = ["flower","flow","flight"]

# def lcp(strs):
#     prefix = {}
#     for i in strs:
#         for j in i:
#             if j in prefix:
#                 prefix[j] += 1
#             else:
#                 prefix[j] = 1
#     print(prefix)



def lcp(strs):
    if len(strs) > 0:
        prefix = strs[0]
    for i in strs:
        for j in i:
            
        

            # prefix += j
    print(prefix)

print(lcp(strs))