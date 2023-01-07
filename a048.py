'''
A048 Group Word Checkers
Problem : https://www.acmicpc.net/problem/1316
Date : 20230107
'''

def check(word):
    dict = {}
    check = []
    for i in word:
        if i not in dict:
            dict[i] = 1
        else:
            value = dict[i]
            del dict[i]
            dict[i] = value + 1
    dict2 = {i:dict[i] for i in dict if dict[i] > 1}
    for j in dict2:
        if j*dict[j] not in word:
            return False
    return True

T = int(input())
count = 0
for i in range(T):
    if check(input()) == True:
        count = count + 1
print(count)