# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        s = 0
        if root is None:return s
        stk = [(root, root.val)]
        while(len(stk)):
            u, v = stk.pop()
            if u.left is None and u.right  is None:
                s += v
            if u.left:
                stk.append( (u.left, v*10 + u.left.val)  )
            if u.right:
                stk.append( (u.right, v*10 + u.right.val) )
            
        return s