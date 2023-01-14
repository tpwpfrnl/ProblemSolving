'''
A070 Card2
Problem : https://www.acmicpc.net/problem/2164
Date : 20230114
'''

from collections import deque

N = int(input())
li = [i for i in range(1, N + 1)]
queue = deque(li)
while len(queue) > 1 :
    queue.popleft()
    queue.append(queue.popleft())
print(queue[0])