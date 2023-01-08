'''
A055 Remove Outermost Parentheses
Problem : https://leetcode.com/problems/remove-outermost-parentheses/
Date : 20230108
'''

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        li = []
        flag = 0
        for i in s:
            if i == "(":
                li.append(flag)
                flag = flag + 1
            else:
                flag = flag - 1
                li.append(flag)
        answer = ""
        for j in range(len(s)):
            if li[j] == 0:
                continue
            answer = answer + s[j]
        return answer