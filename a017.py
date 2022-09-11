'''
A017 Room Number
Problem : https://www.acmicpc.net/problem/1475
Date : 20220912
'''

# number = list(input())
# max = 0
# sweep = (number.count('6')+number.count('9'))
# for i in number:
#     numbnow = number.count(i)
#     if i == '6' or i == '9':
#         continue
#     elif max < numbnow:
#         max = numbnow
# if max < sweep/2 + sweep%2:
#     max = sweep/2 + sweep%2
# print(int(max))

number = list(input())
max = 0
sweep = (number.count('6')+number.count('9'))
for i in range(10):
    numbnow = number.count(str(i))
    if str(i) == '6' or str(i) == '9':
        continue
    elif max < numbnow:
        max = numbnow
if max < sweep/2 + sweep%2:
    max = sweep/2 + sweep%2
print(int(max))
