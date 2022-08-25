'''
A004 Divisible Array of Numbers
Problem : https://school.programmers.co.kr/learn/courses/30/lessons/12910
Date : 20220825
'''

def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    if len(answer) == 0:
        element = -1
        answer.append(element)
    answer.sort()
    return answer