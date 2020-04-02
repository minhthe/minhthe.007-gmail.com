'''
https://leetcode.com/problems/maximum-depth-of-binary-tree/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None : return 0
        def f(root, l):
            stk = [(root, l)]
            ans = 0
            while(len(stk)):
                u, l = stk.pop()
                if(u.left is None and u.right is None):
                    ans = max(ans, l)
                if(u.left): 
                    stk.append((u.left, l + 1))
                if(u.right):
                    stk.append((u.right, l + 1))
            return ans
        return f(root, 1)