'''
A021 Plug
Problem : https://www.acmicpc.net/problem/2010
Date : 20220912
'''

import sys

numb = int(input())
sum = 1
for i in range(numb):
    sum = sum + int(sys.stdin.readline())
print(sum - numb)