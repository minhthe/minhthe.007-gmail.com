'''
https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/


Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

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