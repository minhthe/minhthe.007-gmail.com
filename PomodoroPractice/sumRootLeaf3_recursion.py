'''
https://leetcode.com/problems/sum-root-to-leaf-numbers
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        rst = []
        if root is None: return 0
        def f(root, rst, s):
            if root.left is None and root.right is None :
                rst.append(s)
                return
            if root.left:
                f(root.left, rst, s + str(root.left.val))
            if root.right:
                f(root.right, rst, s + str(root.right.val))
            
            return rst
        
        f(root,rst,str(root.val))
        print(rst)
        return sum([int(item) for item in rst])