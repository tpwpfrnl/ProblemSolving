'''
A081 Nth largest Number
Problem : https://www.acmicpc.net/problem/2693
Date : 20230115
'''

T = int(input())
for i in range(T):
    li = list(map(int, input().split()))
    li = sorted(li, reverse=True)
    print(li[2])