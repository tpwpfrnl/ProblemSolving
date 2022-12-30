'''
A037 Self Dividing Numbers
Problem : https://leetcode.com/problems/self-dividing-numbers/
Date : 20221231
'''

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        div = []
        for i in range(left, right + 1):
            div.append(i)
            strnumb = str(i)
            if '0' in strnumb:
                div.remove(i)
            else:
                for j in strnumb:
                    if i % int(j) != 0:
                        div.remove(i)
                        break
        return div
