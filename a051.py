'''
A051 Dial
Problem : https://www.acmicpc.net/problem/5622
Date : 20230107
'''

word = input()
numb = 0
for i in word:
    if i in "ABC":
        numb = numb + 3
    elif i in "DEF":
        numb = numb + 4
    elif i in "GHI":
        numb = numb + 5
    elif i in "JKL":
        numb = numb + 6
    elif i in "MNO":
        numb = numb + 7
    elif i in "PQRS":
        numb = numb + 8
    elif i in "TUV":
        numb = numb + 9
    elif i in "WXYZ":
        numb = numb + 10
print(numb)