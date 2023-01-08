'''
A063 Add Binary
Problem : https://leetcode.com/problems/add-binary
Date : 20230109
'''

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum = int(a, 2) + int(b, 2)
        return str(bin(sum))[2:]