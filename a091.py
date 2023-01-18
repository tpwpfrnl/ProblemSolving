'''
A091 Remove Element
Problem : https://leetcode.com/problems/remove-element/description/
Date : 20230119
'''

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for i, value in enumerate(nums):
            print(i, value)
            if value == val:
                nums[i] = -1
                count = count + 1
        for j in range(count):
            nums.remove(-1)