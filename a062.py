'''
A062 2016
Problem : https://programmers.co.kr/learn/courses/30/lessons/12901
Date : 20230109
'''

def solution(a, b):
    if a == 1:
        day = b
    elif a == 2:
        day = 31 + b
    elif a == 3:
        day = 31 + 29 + b
    elif a == 4:
        day = 31 + 29 + 31 + b
    elif a == 5:
        day = 31 + 29 + 31 + 30 + b
    elif a == 6:
        day = 31 + 29 + 31 + 30 + 31 + b
    elif a == 7:
        day = 31 + 29 + 31 + 30 + 31 + 30 + b
    elif a == 8:
        day = 31 + 29 + 31 + 30 + 31 + 30 + 31 + b
    elif a == 9:
        day = 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + b
    elif a == 10:
        day = 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + b
    elif a == 11:
        day = 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + b
    elif a == 12:
        day = 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + b
    day = day % 7
    if day == 0:
        answer = "THU"
    elif day == 1:
        answer = "FRI"
    elif day == 2:
        answer = "SAT"
    elif day == 3:
        answer = "SUN"
    elif day == 4:
        answer = "MON"
    elif day == 5:
        answer = "TUE"
    elif day == 6:
        answer = "WED"
    return answer