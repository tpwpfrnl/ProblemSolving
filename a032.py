'''
A032 I Will Become the President of Women's Society
Problem : https://www.acmicpc.net/problem/2775
Date : 20221230
'''

floor = 20
room = 14
howmany = [[0 for j in range(room)] for i in range(floor)]

for i in range(room):
    howmany[0][i] = i + 1

T = int(input())
for i in range(T):
    k = int(input())
    n = int(input())
    
    for l in range(1, k + 1):
        for m in range(14):
            howmany[l][0] = howmany[0][0]
            howmany[l][m] = howmany[l][m - 1] + howmany[l - 1][m]
        
    print(howmany[k][n-1])