'''
B001 Virus
Problem : https://www.acmicpc.net/problem/2606
Date : 20221231
'''

from collections import deque

numbOfCom = int(input())
linklist = [[] for i in range(numbOfCom)]
numbOfLink = int(input())

for i in range(numbOfLink):
    a, b = map(int, input().split())
    linklist[a - 1].append(b)
    linklist[b - 1].append(a)
    
comlist = [False] * numbOfCom
queue = deque([i for i in linklist[0]])

while(len(queue) != 0):
    index = queue[0]
    comlist[index - 1] = True
    for j in linklist[index - 1]:
        if comlist[j - 1] == False:
            queue.append(j)
    queue.popleft()

comlist[0] = False
print(comlist.count(True))