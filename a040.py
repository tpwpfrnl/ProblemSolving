'''
A040 Determine if String Halves Are Alike
Problem : https://leetcode.com/problems/determine-if-string-halves-are-alike/
Date : 20221231
'''

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        halflen = int(len(s)/2)
        a = s[:halflen]
        b = s[halflen:]
        vowela = 0
        vowelb = 0
        for i in a:
            if i in 'aeiouAEIOU':
                vowela = vowela + 1
        for i in b:
            if i in 'aeiouAEIOU':
                vowelb = vowelb + 1
        if vowela == vowelb:
            return True
        return False