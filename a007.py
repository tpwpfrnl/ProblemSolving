'''
A007 Determining the scale
Problem : https://www.acmicpc.net/problem/2920
Date : 20220828
'''
a = input()
if a in "1 2 3 4 5 6 7 8":
    print("ascending")
elif a in "8 7 6 5 4 3 2 1":
    print("descending")
else:
    print("mixed")