'''
https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = None
        
        def f(root, item):
            if root is None:
                root = TreeNode(item)
            else:
                if item < root.val:
                    root.left = f(root.left, item)
                else:
                    root.right = f(root.right, item)
            return root
        for item in preorder:
            root = f(root, item)
        return root