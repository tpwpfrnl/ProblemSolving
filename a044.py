'''
A044 Student Attendance Record I
Problem : https://leetcode.com/problems/student-attendance-record-i/
Date : 20221231
'''

class Solution:
    def checkRecord(self, s: str) -> bool:
        absent = 0
        late = 0
        for i in s:
            if i == 'A':
                absent = absent + 1
                if absent >= 2:
                    return False
            if i == 'L':
                late = late + 1
                if late >= 3:
                    return False
            else:
                late = 0
        return True
