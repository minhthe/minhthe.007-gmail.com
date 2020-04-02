'''
https://leetcode.com/problems/minimum-depth-of-binary-tree/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        def f(root,l):
            if(root is None): return 0
            stk = [(root,l)]
            ans = int(1e9)
            while(len(stk)):
                u, l = stk.pop()
                if(u.left is None and u.right is None):
                    ans = min(l, ans)
                if(u.left):
                    stk.append((u.left, l + 1))
                if(u.right):
                    stk.append((u.right, l + 1))
            return ans
        return f(root, 1)
        