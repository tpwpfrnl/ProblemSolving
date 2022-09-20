'''
A030 Good Days and Bad Days
Problem : https://www.acmicpc.net/problem/17211
Date : 20220921
'''

number, today = map(int, input().split())
gg, gb, bg, bb = list(map(float, input().split()))

if today == 0:
    good = gg
    bad = gb
elif today == 1:
    good = bg
    bad = bb
goodl = [good]
badl = [bad]
for i in range(number - 1):
    goodl.append(goodl[i] * gg + badl[i] * bg)
    badl.append(goodl[i] * gb + badl[i] * bb)
goodday = goodl[-1] * 1000
badday = badl[-1] * 1000
if goodday % 1 >= 0.5:
    goodday = int(goodday) + 1
if badday % 1 >= 0.5:
    badday = int(badday) + 1
print(int(goodday))
print(int(badday))