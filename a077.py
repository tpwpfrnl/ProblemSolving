'''
A077 Scoring
Problem : https://www.acmicpc.net/problem/2822
Date : 20230115
'''

li = []
for i in range(8):
    li.append([int(input()), i])
li = sorted(li, reverse=True)

ans = 0
ans2 = []
for i in range(5):
    ans = ans + li[i][0]
    ans2.append(li[i][1] + 1)
print(ans)
ans2 = sorted(ans2)
# for i in ans2:
print(" ".join(map(str, ans2)), sep="")