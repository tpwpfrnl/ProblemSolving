'''
A083 Sort Excluding Duplicates
Problem : https://www.acmicpc.net/problem/10867
Date : 20230115
'''

N = int(input())
numbers = {int(i):"" for i in input().split()}
numbers = sorted(numbers.keys())
print(" ".join(map(str, numbers)))