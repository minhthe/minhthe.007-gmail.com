# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None: return True
        stk = [(root, float('-inf'), float('inf'))]
        while stk:
            u , lower, upper = stk.pop()
            if u.val >= upper or u.val <= lower: return False
            if u.left:
                stk.append( (u.left, lower, u.val) )
            if u.right:
                stk.append( (u.right, u.val, upper) )
        return True
                
            