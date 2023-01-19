'''
A100 Range Sum of BST
Problem : https://leetcode.com/problems/range-sum-of-bst/description/
Date : 20230119
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        next = None
        sum = 0
        nxt = [None]
        while root != None:
            if root.left != None:
                if root.right != None:
                    next = root.right
                    nxt.append(next)
                if root.val <= high and root.val >= low:
                    sum = sum + root.val
                root = root.left
            else:
                if root.val <= high and root.val >= low:
                    sum = sum + root.val
                root = nxt.pop()
                
        return sum