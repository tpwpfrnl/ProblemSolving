'''
A067 Remmove All Adjacent Duplicates in String
Problem : https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
Date : 20230108
'''

class Solution:
    def removeDuplicates(self, s: str) -> str:
        now = s[0]
        for i in s[1:]:
            if len(now) != 0 and i == now[-1]:
                now = now[:-1]
            else:
                now = now + i
        return now