'''
A027 Making Largest Number
Problem : https://school.programmers.co.kr/learn/courses/30/lessons/42883#
Date : 20220919
'''

def solution(number, k):
    number = str(number)
    length = len(number) - k
    if length == 1:
        return max(number)
    maxidx = number.find(max(number[:-(length-1)]))
    newnumb = number[maxidx:]
    if len(newnumb) == length:
        return newnumb
    else:
        n = 1
        # for i in range(1, len(newnumb)):
        while n <= length:
            if newnumb[n - 1] < newnumb[n]:
                newnumb = newnumb[:n - 1] + newnumb[n:]
                n = n - 2
                if len(newnumb) == length:
                    return newnumb
            n = n + 1
        newnumb = newnumb[:-1]
        return newnumb

print(solution(6617423282157290684025607883097699259905250470744165128706131448395502185407310941966307933122347117, 61))