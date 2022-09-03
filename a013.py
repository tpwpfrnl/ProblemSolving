'''
A013 Single Number
Problem : https://leetcode.com/problems/single-number/
Date : 20220904
'''

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        for i in nums:
            if nums.count(i) == 1:
                return i