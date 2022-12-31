'''
A039 Valid Perfect Square
Problem : https://leetcode.com/problems/valid-perfect-square/
Date : 20221231
'''

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        for i in range(num):
            if i * i < num:
                continue
            elif i * i == num:
                return True
            else:
                return False