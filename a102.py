'''
A102 Transpose Matrix
Problem : https://leetcode.com/problems/transpose-matrix/
Date : 20230119
'''

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        new = [[] * len(matrix) for i in range(len(matrix[0]))]
        for idx, line in enumerate(matrix):
            for idx2, j in enumerate(line):
                new[idx2].append(j)
        return new