'''
A033 I am a Cook
Problem : https://www.acmicpc.net/problem/2953
Date : 20221230
'''

max = 0
index = 0

for i in range(5):
    score = 0
    n = map(int, input().split())
    for j in n:
        score = score + j
    if max < score:
        max = score
        index = i + 1

print(index, max)