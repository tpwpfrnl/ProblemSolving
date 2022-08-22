class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        a = ""
        for i in digits:
            a = a + str(i)
        b = int(a) + 1
        newdigits = [j for j in str(b)]
        return newdigits

a = Solution()
print(a.plusOne([9,9]))