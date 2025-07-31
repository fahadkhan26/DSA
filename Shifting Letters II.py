# s = "dztz"
# shifts = [[0,0,0],[1,1,1]]

# def shiftingletters(s, shifts):
#     ascii_s = [ord(i) for i in s]
#     print(ascii_s)

#     for i in shifts:
#         # print(i, "i")
#         print(i, "i")
#         if i[2] == 1:
#             for j in range(i[0], i[1]+1, 1):
#                 print(j, "1j")
#                 if ascii_s[j] + 1 == ord("z") + 1:
#                     ascii_s[j] = ord("a")
#                 else:
#                     ascii_s[j] += 1
#         else:
#             for j in range(i[0], i[1]+1, 1):
#             # for j in i[0:2]:
#                 print(j, "2j")
#                 print(ascii_s[j]) 
#                 if ascii_s[j] - 1 == ord("a") - 1:
#                     ascii_s[j] = ord("z")
#                 else:
#                     ascii_s[j] -= 1
#         print(ascii_s)
    
#     return "".join([chr(i) for i in ascii_s])

# # print(ord("abc"[0]))
# print(shiftingletters(s, shifts))


# s = "abc"
# shifts = [[0,1,0],[1,2,1],[0,2,1]]

# def shiftingletters(s, shifts):
#     ascii_s = [ord(i) for i in s]
#     print(ascii_s)

#     for start, end, direction in shifts:
#         if direction == 0:

   

# print(shiftingletters(s, shifts))
