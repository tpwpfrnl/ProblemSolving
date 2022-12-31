'''
A046 Basketball Game
Problem : https://www.acmicpc.net/problem/1159
Date : 20221231
'''

T = int(input())
dic = {}
for i in range(T):
    name = str(input())
# for i in string:
    if name[0] not in dic:
        dic[name[0]] = 1
    else:
        val = dic[name[0]]
        del dic[name[0]]
        dic[name[0]] = val + 1
player = []

for key in dic:
    if dic[key] >= 5:
        player.append(key)

if len(player) == 0:
    print("PREDAJA")
else:
    print(''.join(sorted(player)))