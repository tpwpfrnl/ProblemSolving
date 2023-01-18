'''
A092 Sort Array By Parity II
Problem : https://leetcode.com/problems/sort-array-by-parity-ii/description/
Date : 20230119
'''

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd = []
        even = []
        newnums = []
        for i in nums:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        for i in range(len(nums)):
            if i % 2 == 0:
                newnums.append(even[i//2])
            else:
                newnums.append(odd[i//2])
        return newnums