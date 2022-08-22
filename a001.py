'''
A001 Assign Cookies
Problem : https://leetcode.com/problems/assign-cookies/
Date : 20220822
'''

class Solution:
    # g = minimum greed cookie size list, s = cookie size list
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        idx = 0
        # number of cookies that fits the greed
        find = 0
        for i in range(len(s)):
            # if idx is out of len(g) or len(s) == 0, break
            if idx >= len(g) or len(s) == 0:
                break
            if g[idx] <= s[0]:
                idx = idx + 1
                find = find + 1
                del s[0]
            else:
                del s[0]
        print(find)
        return find

a = Solution()
a.findContentChildren([250,490,328,149,495,325,314,360,333,418,430,458],[376,71,228,110,215,410,363,135,508,268,494,288,24,362,20,5,247,118])