'''
A019 Number of Numbers
Problem : https://www.acmicpc.net/problem/2577
Date : 20220912
'''

a = int(input())
b = int(input())
c = int(input())
multi = str(a * b * c)
for i in range(10):
    print(multi.count(str(i)))