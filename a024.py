'''
A024 Lemonade Change
Problem : https://leetcode.com/problems/lemonade-change/
Date : 20220914
'''

class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        d5 = []
        d10 = []
        for i in bills:
            if i == 5:
                d5.append(i)
            elif i == 10:
                d10.append(i)
                if len(d5) == 0:
                    return False
                d5.pop()
            elif i == 20:
                if len(d10) == 0 and len(d5) > 2:
                    d5.pop()
                    d5.pop()
                    d5.pop()
                elif len(d10) != 0 and len(d5) != 0:
                    d5.pop()
                    d10.pop()
                else:
                    return False
        return True