'''
https://leetcode.com/problems/diameter-of-binary-tree/
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None: return 0
        
        def f(root):
            if root is None: return 0
            
            return max(  f(root.left), f(root.right) ) + 1 
            
        l = f(root.left)
        r = f(root.right)
        # print(l, r)
        return max(l + r, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))