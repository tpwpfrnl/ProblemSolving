'''
A020 Intelligent Train
Problem : https://www.acmicpc.net/problem/2455
Date : 20220912
'''

platform1 = list(map(int, input().split()))
platform2 = list(map(int, input().split()))
platform3 = list(map(int, input().split()))
platform4 = list(map(int, input().split()))
train = platform1 + platform2 + platform3 + platform4
now = 0
max = 0
for i in range(len(train)):
    if i % 2 == 1:
        now = now + train[i]
        if max < now:
            max = now
    else:
        now = now - train[i]
print(max)
