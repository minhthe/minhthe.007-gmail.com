'''
https://leetcode.com/problems/same-tree/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None: return True
        
        if p and q :
            if p.val == q.val :
                a = self.isSameTree(p.left, q.left)
                b = self.isSameTree(p.right, q.right)
                return a and b
            else:
                return False
        return False
                