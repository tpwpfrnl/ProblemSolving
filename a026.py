'''
A026 Harshad Number
Problem : https://school.programmers.co.kr/learn/courses/30/lessons/12947
Date : 20220916
'''

def solution(x):
    orig = x
    x = list(map(int,str(x)))
    plus = sum(x)
    if orig % plus == 0:
        return True
    return False