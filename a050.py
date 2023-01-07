'''
A050 Caesar Cipher
Problem : https://www.acmicpc.net/problem/5598
Date : 20230107
'''

word = input()
caesar1 = [i for i in "DEFGHIJKLMNOPQRSTUVWXYZABC"]
caesar2 = [i for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
caesar = dict(zip(caesar1, caesar2))
newword = ""
for i in word:
    newword = newword + caesar[i]
print(newword)