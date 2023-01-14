'''
A072 Day of the Year
Problem : https://leetcode.com/problems/day-of-the-year/
Date : 20230114
'''

class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day = map(int, date.split('-'))
        if month == 1:
            answer = day
        elif month == 2:
            answer = 31 + day
        elif month == 3:
            answer = 31 + 28 + day
        elif month == 4:
            answer = 31 + 28 + 31 + day
        elif month == 5:
            answer = 31 + 28 + 31 + 30 + day
        elif month == 6:
            answer = 31 + 28 + 31 + 30 + 31 + day
        elif month == 7:
            answer = 31 + 28 + 31 + 30 + 31 + 30 + day
        elif month == 8:
            answer = 31 + 28 + 31 + 30 + 31 + 30 + 31 + day
        elif month == 9:
            answer = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + day
        elif month == 10:
            answer = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + day
        elif month == 11:
            answer = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + day
        elif month == 12:
            answer = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + day
        if year % 4 == 0 and month > 2 and year != 1900:
            answer = answer + 1
        return answer