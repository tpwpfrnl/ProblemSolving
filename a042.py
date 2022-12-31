'''
A042 Backspace String Compare
Problem : https://leetcode.com/problems/backspace-string-compare/
Date : 20221231
'''

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1 = ""
        for i in s:
            if i != "#":
                s1 = s1 + i
            else:
                s1 = s1[:-1]
        t1 = ""
        for i in t:
            if i != "#":
                t1 = t1 + i
            else:
                t1 = t1[:-1]
        if s1 == t1:
            return True
        return False