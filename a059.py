'''
A059 Paper
Problem : https://www.codeground.org/practice﻿
Date : 20230109
'''

import sys

#inf = open('input.txt');
inf = sys.stdin 

T = inf.readline()

Answer=0

for t in range(0, int(T)):
    N, K = map(int, input().split())
    scores = list(map(int, input().split()))
    scores = sorted(scores, reverse=True)
    
for i in range(K):
    Answer = Answer + scores[i]
    
print('Case #%d' %(int(t)+ 1))
print(Answer)
inf.close()