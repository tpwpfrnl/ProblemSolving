'''
A034 Remain
Problem : https://www.acmicpc.net/problem/3052
Date : 20221230
'''

remain = []

for i in range(10):
    a = int(input())
    b = a % 42
    if b not in remain:
        remain.append(b)

print(len(remain))