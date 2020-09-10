# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        track = [False]
        def check(root):
            if root.left is None and root.right is None: return 1
            height_left, height_right = 0 , 0
            if root.left:
                height_left = check(root.left)
            if root.right:
                height_right = check(root.right)
            if abs(height_right - height_left) > 1: 
                
                track[0] = [True]
                
            if track[0] == False:
                level =  max(height_right, height_left) + 1
                return level
            return False
         
        ans = check(root)
        if track[0]: return False
        return True