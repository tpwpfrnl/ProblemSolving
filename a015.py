'''
A015 Number of Verifications
Problem : https://www.acmicpc.net/problem/2475
Date : 20220905
'''

number = input().split(' ')
sum = 0
for i in number:
    sum = sum + int(i) * int(i)
spec = sum % 10
print(spec)
