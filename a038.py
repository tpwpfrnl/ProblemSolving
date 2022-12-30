'''
A038 Sqrt(x)
Problem : https://leetcode.com/problems/sqrtx/
Date : 20221231
'''

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        for i in range(x):
            if i * i <= x:
                continue
            else:
                return i - 1
        return 1