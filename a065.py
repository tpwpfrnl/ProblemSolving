'''
A065 Align Coordinates
Problem : https://www.acmicpc.net/problem/11650
Date : 20230108
'''

# T = int(input())
# x = {}
# for index in range(T):
#     y = []
#     point = input().split()
#     point[0] = int(point[0])
#     point[1] = int(point[1])
#     if point[0] in x:
#         y = x[point[0]] + [point[1]]
#         # del x[point[0]]
#     else:
#         y.append(point[1])
#     x[point[0]] = y
    
# sortx = sorted(x.keys())
# for i in sortx:
#     li = x[i]
#     li = sorted(li)
#     for j in li:
#         print(i, j)
T = int(input())
arr = []
for i in range(T):
    arr.append(list(map(int, input().split())))
arr = sorted(arr)
for j in arr:
    print(j[0], j[1])