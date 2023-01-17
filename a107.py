'''
A107 Easy Problem
Problem : https://www.acmicpc.net/problem/1292
Date : 20230118
'''

a, b = map(int, input().split())
numbers = []
answer = 0
for i in range(1, 50):
    numbers = numbers + [i] * i
for i in range(a, b + 1):
    answer = answer + numbers[i - 1]
print(answer)