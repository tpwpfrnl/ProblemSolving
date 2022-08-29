'''
A008 Might be above the Average
Problem : https://www.acmicpc.net/problem/4344
Date : 20220829
'''

numOfTestcase = input()

for i in range(int(numOfTestcase)):
    testcase = list(map(int, input().split()))
    avg = 0
    num = 0
    avg = sum(testcase[1:])/testcase[0]
    for j in range(testcase[0]):
        if testcase[1 + j] > avg:
            num = num + 1
    ratio = (num * 100)/testcase[0]
    print('{:.3f}'.format(ratio)+"%")