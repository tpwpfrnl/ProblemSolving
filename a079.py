'''
A079 Kth Number
Problem : https://school.programmers.co.kr/learn/courses/30/lessons/42748
Date : 20230115
'''

def solution(array, commands):
    answer = []
    for comm in commands:
        newlist = array[comm[0]-1:comm[1]]
        newlist = sorted(newlist)
        answer.append(newlist[comm[2] - 1])
    return answer