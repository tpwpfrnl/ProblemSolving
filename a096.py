'''
A096 Number of 1 Bits
Problem : https://leetcode.com/problems/number-of-1-bits/description/
Date : 20230119
'''

class Solution:
    def hammingWeight(self, n: int) -> int:
        number = str(bin(n))
        count = 0
        for i in number:
            if i == '1':
                count = count + 1
        return count