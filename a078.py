'''
A078 H-Index
Problem : https://school.programmers.co.kr/learn/courses/30/lessons/42747
Date : 20230115
'''

def solution(citations):
    citations = sorted(citations, reverse=True)
    print(citations)
    for i in range(len(citations)):
        if i + 1 == citations[i]:
            return citations[i]
        if i + 1 > citations[i]:
            return i
    if len(citations) > 0 and citations[0] != 0:
        return len(citations)
    answer = 0
    return answer

print(solution([10000, 9999, 9998, 9997, 9996]))