'''
A025 Power of Four
Problem : https://leetcode.com/problems/power-of-four/
Date : 20220915
'''

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1:
            return False
        elif n == 1:
            return True
        while n > 1:
            if n % 4 != 0:
                return False
            n = n // 4
        return True