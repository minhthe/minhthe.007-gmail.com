'''
https://leetcode.com/problems/minimum-depth-of-binary-tree

'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def f(root):
            q = [(root, 1)]
            while(len(q)):
                u, l = q.pop(0)
                if(u.left is None and u.right is None):
                    return l
                if(u.left):
                    q.append((u.left, l + 1))
                if(u.right):
                    q.append((u.right, l + 1))
                    
        return f(root) if root is not None else 0