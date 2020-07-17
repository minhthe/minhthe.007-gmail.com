'''
https://leetcode.com/problems/same-tree
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
        left, right = False, False
        if p and q and  p.val == q.val : 
            left = self.isSameTree(p.left, q.left)
        
            right = self.isSameTree(p.right, q.right)
        
        if left and right: return True
        return False