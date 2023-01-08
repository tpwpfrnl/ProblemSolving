'''
A058 Reverse Linked List
Problem : https://leetcode.com/problems/reverse-linked-list/
Date : 20230109
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        last = None
        while head != None:
            nextv = head.next
            head.next = last
            last = head
            if nextv == None:
                break
            head = nextv
        return head