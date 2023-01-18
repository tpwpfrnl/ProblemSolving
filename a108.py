'''
A108 Flip Number
Problem : https://www.acmicpc.net/problem/3062
Date : 20230119
'''

n = int(input())
for i in range(n):
    numb = str(input())
    revnumb = numb[::-1]
    sum = int(numb) + int(revnumb)
    length = len(str(sum))
    for j in range(int(length/2)):
        if str(sum)[j] != str(sum)[length - 1 - j]:
            print("NO")
            break
        if j == int(length/2) - 1:
            print("YES")