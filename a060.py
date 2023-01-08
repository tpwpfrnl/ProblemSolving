'''
A060 Baseball Game
Problem : https://leetcode.com/problems/baseball-game
Date : 20230109
'''

class Solution:
    def calPoints(self, operations: list[str]) -> int:
        score = []
        for i in operations:
            if i == "+":
                score.append(score[-1] + score[-2])
            elif i == "D":
                score.append(score[-1] * 2)
            elif i == "C":
                score.pop()
            else:
                score.append(int(i))
        print(score)
        return sum(score)