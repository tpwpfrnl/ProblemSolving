'''
A084 Suffix Array
Problem : https://www.acmicpc.net/problem/11656
Date : 20230115
'''

string = input()
stringli = [string[i:] for i in range(len(string) - 1)]
stringli.append(string[-1])
stringli = sorted(stringli)
for i in stringli:
    print(i)