'''
D002 ACM Hotel
Problem : https://www.acmicpc.net/problem/10250
Date : 20221231
'''

T = int(input())
for i in range(T):
    H, W, N = map(int, input().split())
    floor = (N % H) * 100
    room = (N // H) + 1
    if N % H == 0:
        floor = H * 100
        room = N // H
    assign = floor + room
    print(assign)
