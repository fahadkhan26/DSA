# arr = [1,0,2,3,0,4,5,0]

# arr = arr[0:2] + [0] + arr[2:]
# arr.pop()
# arr[2] = 0

# print(arr)


# def dupzeros(arr):
#     for i in range(len(arr)):
#         if arr[i] == 0:
#             arr.pop()
#             arr = arr[0:i] + [0] + arr[i:]
#     print(arr)

# print(dupzeros(arr))


arr = [1,0,2,3,0,4,5,0]
def dupzeros(arr):
    p1 = 0

    while p1 < len(arr):
        if arr[p1] == 0:
            arr.pop()
            arr = arr[0:p1] + [0] + arr[p1:]
            p1 += 2
        else:
            p1 += 1
    return arr

print(dupzeros(arr))