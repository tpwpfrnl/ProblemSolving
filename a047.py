'''
A047 Print in Ten
Problem : https://www.acmicpc.net/problem/11721
Date : 20221231
'''

string = str(input())
str = ""
for i in string:
    str = str + i
    if len(str) == 10:
        print(str)
        str = ""
if len(str) != 0:
    print(str)