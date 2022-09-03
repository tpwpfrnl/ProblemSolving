'''
A014 Summary Ranges
Problem : https://leetcode.com/problems/summary-ranges/
Date : 20220904
'''

class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        answer = []
        if len(nums) == 0 or len(nums) == 1:
            return map(str, nums)
        count = nums[0]
        start = nums[0]
        flag = 0
        for i in nums[1:]:
            if i == count + 1:
                if i == nums[-1]:
                    end = i
                else:
                    count = count + 1
                    continue
            else:
                end = count
                if i == nums[-1]:
                    flag = -1
            if start == end:
                element = str(start)
            else:
                element = str(start)+"->"+str(end)
            answer.append(element)
            start = i
            count = i
            if flag == -1:
                answer.append(str(i))
        return answer