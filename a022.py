'''
A022 Cell Phone Bill
Problem : https://www.acmicpc.net/problem/1267
Date : 20220912
'''

numb = int(input())
call = list(map(int, input().split()))
y = 0
m = 0
for i in range(len(call)):
    if i % 60 == 30:
        y = y + (call[i]//30 + 1) * 10
        m = m + (call[i]//60) * 15
    else:
        y = y + (call[i]//30 + 1) * 10
        m = m + (call[i]//60 + 1) * 15
if y < m:
    print("Y " + str(y))
elif y > m:
    print("M " + str(m))
else:
    print("Y M " + str(m))