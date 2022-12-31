'''
A041 Create JadenCase Strings
Problem : https://programmers.co.kr/learn/courses/30/lessons/12951
Date : 20221231
'''

def solution(s):
    news = s[0]
    if news.isalpha() == True:
        news = news.upper()
    last = s[0]
    for cha in s[1:]:
        # if cha.isalpha() == False:
            # news = news + cha
        if last == " ":
            news = news + cha.upper()
        else:
            news = news + cha.lower()
        last = cha
    return news