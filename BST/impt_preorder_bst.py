'''
https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        
        def insertNode(root, item):
            if root is None:
                root = TreeNode(item)
            else:
                if(root.val > item):
                    root.left = insertNode(root.left, item)
                else:
                    root.right = insertNode(root.right, item)
            return root
        root = None
        for item in preorder:
            root = insertNode(root, item)
        return root