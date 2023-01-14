'''
A071 Implement Queue using Stacks
Problem : https://leetcode.com/problems/implement-queue-using-stacks
Date : 20230114
'''

class MyQueue:

    def __init__(self):
        self.li = []

    def push(self, x: int) -> None:
        self.li.append(x)

    def pop(self) -> int:
        return self.li.pop(0)

    def peek(self) -> int:
        return self.li[0]

    def empty(self) -> bool:
        if len(self.li) == 0:
            return True
        else:
            return False

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()