'''
A005 Skill Trees
Problem : https://school.programmers.co.kr/learn/courses/30/lessons/49993
Date : 20220826
'''

def solution(skill, skill_trees):
    answer = 0
    
    for tree in skill_trees:
        element = ""
        for j in tree:
            if j in skill:
                element = element + j
                
        if element in skill:
            if len(element) != 0 and element[0] != skill[0]:
                continue
            answer = answer + 1
            print(element)
            
    return answer

print(solution("CBD",["BACDE", "CBADF", "AECB", "BDA", "AE", "CAD"]))