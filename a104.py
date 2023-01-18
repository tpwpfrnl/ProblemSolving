'''
A104 Ukje is a Filial Piety!!
Problem : https://www.acmicpc.net/problem/14487
Date : 20230119
'''

towns = int(input())
val = list(map(int, input().split()))
print(sum(val) - max(val))