'''
A016 Lifeboat
Problem : https://school.programmers.co.kr/learn/courses/30/lessons/42885
Date : 20220907
'''

# def solution(people, limit):
#     people.sort()
#     length = len(people)
#     li = ["unknown"] * length
#     for i in range(length):
#         if limit - people[i] < people[0]:
#             li[i] = "alone"
#     for i in range(length):
#         if li[length-1] != "unknown":
#             length = length -1
#         if li[i] != "unknown":
#             continue
#         for j in range(length - 1, i, -1):
#             if li[j] != "unknown":
#                 continue
#             elif people[i] + people[j] > limit:
#                 continue
#             li[i] = "together"
#             li[j] = "together"
#             break
#     return len(li) - int(li.count("together")/2)

def solution(people, limit):
    people.sort(reverse = True)
    length = len(people)
    alone = [i for i in people if limit - i < people[-1]]
    answer = len(alone)
    end = length - 1
    for i in range(len(alone), length):
        # print(i,end)
        answer = answer + 1
        if people[i] + people[end] <= limit:
            end = end - 1
        if i >= end:
            break
    return answer


print(solution([70, 50, 80, 50], 100)) #ans:4