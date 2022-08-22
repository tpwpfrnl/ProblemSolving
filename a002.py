'''
A001 Pascal's Triangle
Problem : https://leetcode.com/problems/pascals-triangle/
Date : 20220823
'''

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        pascal = []
        for i in range(numRows):
            row = []
            for j in range(i+1):
                elem = 1
                if i >= 2 and j > 0 and j < i:
                    elem = pascal[i - 1][j - 1] + pascal[i - 1][j]
                row.append(elem)
            pascal.append(row)
        return pascal

a = Solution()
print(a.generate(5))