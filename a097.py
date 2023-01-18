'''
A097 Two Sum II - Input Array Is Sorted
Problem : https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
Date : 20230119
'''

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, a in enumerate(numbers):
            if i > 0 and a == numbers[i - 1]:
                continue
            for j, b in enumerate(numbers[i+1:]):
                if a + b > target:
                    break
                elif a + b == target:
                    print(a, b)
                    return [i+1] + [i + j + 1 + 1]