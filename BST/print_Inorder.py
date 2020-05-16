'''
https://leetcode.com/problems/binary-tree-inorder-traversal/

All 3 ways:
iteration 
recurison 
not 2 above 
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # inorder left root right
        def f(tree):
            if(tree is None):
                return []
            else:
                return f(tree.left) + [tree.val] + f(tree.right)
        return f(root)