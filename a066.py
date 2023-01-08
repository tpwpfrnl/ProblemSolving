'''
A066 Sort Inside
Problem : https://www.acmicpc.net/problem/1427
Date : 20230108
'''

numb = list(input())
numb = sorted(numb, reverse=True)
answer = ""
for i in numb:
    answer = answer + i
print(answer)