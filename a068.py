'''
A068 Queue 2
Problem : https://www.acmicpc.net/problem/18258
Date : 20230114
'''

from collections import deque
import sys

queue1 = []
queue = deque(queue1)
N = int(sys.stdin.readline())
for i in range(N):
    command = sys.stdin.readline()[:-1]
    if command == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif command == 'size':
        print(len(queue))
    elif command == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif command == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif command == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
    else:
        numb = command.split()[1]
        queue.append(numb)