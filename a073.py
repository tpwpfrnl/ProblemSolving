'''
A073 Fizz Buzz
Problem : https://leetcode.com/problems/fizz-buzz/
Date : 20230114
'''

class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        output = [i for i in range(1, n + 1)]
        for i in output:
            if i % 5 == 0 and i % 3 == 0:
                output[i - 1] = "FizzBuzz"
            elif i % 3 == 0:
                output[i - 1] = "Fizz"
            elif i % 5 == 0:
                output[i - 1] = "Buzz"
            else:
                output[i - 1] = str(i)
        return output