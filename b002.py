'''
B002 Employee Importance
Problem : https://leetcode.com/problems/employee-importance/
Date : 20221231
'''

from collections import deque

class Employee:
    def __init__(self, id: int, importance: int, subordinates: list[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees: list['Employee'], id: int) -> int:
        for i in employees:
            if i.id == id:
                sum = i.importance
                queue = deque(i.subordinates)
                break
        while(len(queue) != 0):
            index = queue[0]
            for j in employees:
                if j.id == index:
                    sum = sum + j.importance
                    queue = queue + deque(k for k in j.subordinates)
            queue.popleft()
        return sum