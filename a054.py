'''
A054 Crane Catch Game
Problem : https://school.programmers.co.kr/learn/courses/30/lessons/64061
Date : 20230108
'''

def solution(board, moves):
    size = len(board)
    top = [-1] * size
    for i, line in enumerate(board):
        for j, entry in enumerate(line):
            if entry != 0 and top[j] == -1:
                top[j] = i
    bucket = []
    for move in moves:
        if top[move - 1] < size:
            bucket.append(board[top[move - 1]][move - 1])
            top[move - 1] = top[move - 1] + 1
    stack = []
    answer = 0
    for doll in bucket:
        if len(stack) == 0:
            stack.append(doll)
        elif stack[-1] == doll:
            stack.pop()
            answer = answer + 2
        else:
            stack.append(doll)
    return answer

# board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
# moves = [1,5,3,5,1,2,1,4]
board = [[0,1],[1,1]]
moves = [2,2]
print(solution(board, moves))