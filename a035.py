'''
A035 Mars Math
Problem : https://www.acmicpc.net/problem/5355
Date : 20221230
'''

T = int(input())
for i in range(T):
    case = list(map(str, input().split()))
    numb = float(case[0])
    for j in case[1:]:
        if j == '@':
            numb = numb * 3
        elif j == '%':
            numb = numb + 5
        elif j == '#':
            numb = numb - 7
    print('%.2f' %numb)