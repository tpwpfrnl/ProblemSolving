'''
A018 Treasure
Problem : https://www.acmicpc.net/problem/1026
Date : 20220912
'''

leng = int(input())
arrayA = list(map(int, input().split()))
arrayB = list(map(int, input().split()))
arrayA.sort()
sum = 0

for i in range(leng):
    sum = sum + arrayA[i] * max(arrayB)
    arrayB.remove(max(arrayB))
print(sum)