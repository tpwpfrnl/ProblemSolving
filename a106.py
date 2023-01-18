'''
A106 Sum of Non-appearing Characters
Problem : https://www.acmicpc.net/problem/3059
Date : 20230118
'''

N = int(input())
for i in range(N):
    lis = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    answer = 0
    str = input()
    for idx, j in enumerate(str):
        if j in lis:
            lis.remove(j)
    for j in lis:
        answer = answer + ord(j)
    print(answer)