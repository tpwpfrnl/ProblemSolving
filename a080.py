'''
A080 Majority Element
Problem : https://leetcode.com/problems/majority-element/
Date : 20230115
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums = sorted(nums)
        return nums[len(nums)//2]