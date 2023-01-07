'''
A049 Pronounce Password
Problem : https://www.acmicpc.net/problem/4659
Date : 20230107
'''

def quality(word):
    cons = 0
    new = ""
    for i in word:
        if i in "aeiou":
            cons = cons + 1
            new = new + "0"
        else:
            new = new + "1"
    if cons == 0:
        return False
    if "000" in new or "111" in new:
        return False
    la = word[0]
    for i in word[1:]:
        if la == i and i not in "eo":
            return False
        la = i
    return True

word = input()
while word != "end":
    if quality(word) == True:
        print("<"+word+"> is acceptable.")
    else:
        print("<"+word+"> is not acceptable.")
    word = input()