'''
A052 OX Quiz
Problem : https://www.acmicpc.net/problem/8958
Date : 20230107
'''

T = int(input())
for i in range(T):
    quiz = input()
    score = 0
    cont = 0
    last = quiz[0]
    for j in quiz:
        if last == j:
            cont = cont + 1
        if j == "O":
            score = score + cont
            if cont == 0:
                score = score + 1
                cont = 1
        else:
            cont = 0
        last = j
    print(score)