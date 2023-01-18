'''
A094 Croatian Alphabet
Problem : https://www.acmicpc.net/problem/2941
Date : 20230119
'''

string = input()
if 'c=' in string:
    string = string.replace('c=', 'c')
if 'c-' in string:
    string = string.replace('c-', 'c')
if 'dz=' in string:
    string = string.replace('dz=', 'd')
if 'd-' in string:
    string = string.replace('d-', 'd')
if 'lj' in string:
    string = string.replace('lj', 'l')
if 'nj' in string:
    string = string.replace('nj', 'n')
if 's=' in string:
    string = string.replace('s=', 's')
if 'z=' in string:
    string = string.replace('z=', 'z')
print(len(string))