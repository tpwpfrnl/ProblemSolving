'''
A093 Merge Sorted Array
Problem : https://leetcode.com/problems/merge-sorted-array/description/
Date : 20230119
'''

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2
        nums1.sort()