'''
A087 Maximum Units on a Truck
Problem : https://leetcode.com/problems/maximum-units-on-a-truck/description/
Date : 20230115
'''

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:x[1], reverse=True)
        print(boxTypes)
        answer = 0
        while truckSize > 0:
            for i in boxTypes:
                if i[0] <= truckSize:
                    answer = answer + i[0]*i[1]
                    truckSize = truckSize - i[0]
                else:
                    answer = answer + truckSize*i[1]
                    break
            return answer