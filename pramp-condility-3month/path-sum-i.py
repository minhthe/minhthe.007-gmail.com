'''https://leetcode.com/problems/path-sum'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None: return False
        stk = [(root, root.val)]
        while stk:
            u,v = stk.pop()
            if u.left is None and u.right is None and v == sum:
                return True
            if u.left:
                stk.append( (u.left, u.left.val + v) )
            if u.right:
                stk.append( (u.right, u.right.val + v) )
        return False