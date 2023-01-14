'''
A074 Valid Palindrome
Problem : https://leetcode.com/problems/valid-palindrome/
Date : 20230114
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True
        newstr = [i.upper() for i in s if i.isalpha() == True or i.isdigit() == True]
        for i in range(len(newstr) // 2):
            if newstr[i] != newstr[len(newstr) - 1 - i]:
                return False
        return True