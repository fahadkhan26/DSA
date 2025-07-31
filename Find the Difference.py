# s = "abcd"
# t = "abcde"

# def difference(s, t):
#     sd = {}
#     td = {}
#     for i in s:
#         if i in sd:
#             sd[i] += 1
#         else:
#             sd[i] = 1
#     for i in t:
#         if i in td:
#             td[i] += 1
#         else:
#             td[i] = 1
    
#     return

# print(difference(s, t))


s = "abcd"
t = "abcde"


def difference(s, t):
    x = max(len(s),len(t))
    print(x)
print(difference(s, t))