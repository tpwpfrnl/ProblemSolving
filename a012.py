'''
A012 Count Primes
Problem : https://leetcode.com/problems/count-primes/
Date : 20220904
'''

class Solution:
    def countPrimes(self, n: int) -> int:
        t = [False,False]+[True]*(n-2)
        for i in range(2, n):
            if t[i] == False:
                continue
            for j in range(i * 2, n, i):
                t[j] = False
        return t.count(True)

a = Solution()
print(a.countPrimes(400000))