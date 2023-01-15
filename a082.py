'''
A082 Sort by Age
Problem : https://www.acmicpc.net/problem/10814
Date : 20230115
'''

N = int(input())
members = []
for i in range(N):
    age, name = input().split()
    members.append([int(age), name])
members.sort(key=lambda x:x[0])
for i, j in members:
    print(i, j)