'''
A023 Add Digits
Problem : https://leetcode.com/problems/add-digits/
Date : 20220913
'''

class Solution:
    def addDigits(self, num: int) -> int:
        digits = str(num)
        add = 0
        while True:
            add = 0
            for i in digits:
                add = add + int(i)
            digits = str(add)
            if len(str(add)) == 1:
                break
        return add