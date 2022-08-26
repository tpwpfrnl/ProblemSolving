'''
A006 Skill Trees
Problem : https://school.programmers.co.kr/learn/courses/30/lessons/12916
Date : 20220826
'''

def solution(s):
    numP = 0
    numY = 0
    for i in s:
        if i in "pP":
            numP = numP + 1
        elif i in "yY":
            numY = numY + 1
    if numP == numY:
        return True
    return False
