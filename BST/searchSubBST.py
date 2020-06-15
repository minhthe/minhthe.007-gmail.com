''''
https://leetcode.com/problems/search-in-a-binary-search-tree/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None: return None
        def f(root):
            if root:
                if root.val == val: 
                    return root
                if root.val > val and  root.left:
                    return f(root.left)
                if root.right:
                    return f(root.right)
            return None
            
        ans  = f(root)
        return ans