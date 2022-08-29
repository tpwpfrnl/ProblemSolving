'''
A009 String Handling Basics
Problem : https://school.programmers.co.kr/learn/courses/30/lessons/12918
Date : 20220829
'''

def solution(s):
    if (len(s) != 4 and len(s) != 6) or not s.isdigit():
        return False
    return True

print(solution("1234"))