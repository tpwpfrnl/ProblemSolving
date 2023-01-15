'''
A085 Serial Number
Problem : https://www.acmicpc.net/problem/1431
Date : 20230115
'''

start, last = input().split()
numbslist = [i for i in range(int(start), int(last) + 1)]
newn = {}
for i in numbslist:
    numbstr = ""
    for j in str(i):
        if j == "0":
            numbstr = numbstr + "zero"
        elif j == "1":
            numbstr = numbstr + "one"
        elif j == "2":
            numbstr = numbstr + "two"
        elif j == "3":
            numbstr = numbstr + "three"
        elif j == "4":
            numbstr = numbstr + "four"
        elif j == "5":
            numbstr = numbstr + "five"
        elif j == "6":
            numbstr = numbstr + "six"
        elif j == "7":
            numbstr = numbstr + "seven"
        elif j == "8":
            numbstr = numbstr + "eight"
        elif j == "9":
            numbstr = numbstr + "nine"
    newn[int(i)] = numbstr
newn = sorted(newn.items(), key = lambda item: item[1])
for i in range(len(newn)):
    print(newn[i][0], end=" ")
    if i % 10 == 9:
        print("")
            