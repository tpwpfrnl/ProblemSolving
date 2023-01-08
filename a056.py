'''
A056 Next Greater Element I
Problem : https://leetcode.com/problems/next-greater-element-i
Date : 20230109
'''

class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> List[int]:
        answer = []
        for i in nums1:
            index = nums2.index(i)
            if index == len(nums2) - 1 or max(nums2[index + 1:]) < nums2[index]:
                answer.append(-1)
            else:
                for j in nums2[index + 1:]:
                    if j > nums2[index]:
                        answer.append(j)
                        break
        return answer