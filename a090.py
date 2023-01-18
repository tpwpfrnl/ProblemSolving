'''
A090 Remove Duplicates from Sorted Array
Problem : https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
Date : 20230117
'''

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        count = 0
        for i, num in enumerate(nums):
            if nums.count(num) > 1:
                nums[i] = -101
                count = count + 1
        for i in range(count):
            nums.remove(-101)