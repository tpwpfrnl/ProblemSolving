'''
A010 String Compression
Problem : https://school.programmers.co.kr/learn/courses/30/lessons/60057
Date : 20220830
'''

def solution(s):
    answer = len(s)
    for i in range(1, len(s)):
        listS = split(s, i)
        for j in range(len(listS)-1):
            if listS[j] == listS[j+1]:
                listS[j] = '2'
                if j != 0 and listS[j-1].isdigit():
                    listS[j] = str(int(listS[j-1])+1)
                    listS[j-1] = ''
        # print(listS)
        stringS = ''.join(listS)
        if len(stringS) < answer:
            answer = len(stringS)
    return answer

def split(s, numb):
    list1 = []
    max = numb
    for i in range(0, len(s), numb):
        if max < len(s):
            list1.append(s[i:i+numb])
        max = i+numb
    return list1

print(solution("cccccccccc"))