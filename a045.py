'''
A045 Word Study
Problem : https://www.acmicpc.net/problem/1157
Date : 20221231
'''

string = str(input()).upper()
dic = {}
for i in string:
    if i not in dic:
        dic[i] = 1
    else:
        val = dic[i]
        del dic[i]
        dic[i] = val + 1
sortdic = sorted(dic.values())
if sortdic.count(sortdic[-1]) > 1:
    print("?")
else:
    for key in dic:
        if dic[key] == sortdic[-1]:
            print(key)