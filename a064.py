'''
A064 Height Checker
Problem : https://leetcode.com/problems/height-checker/
Date : 20230109
'''

class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        expected = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if expected[i] != heights[i]:
                count = count + 1
        return count