'''
https://leetcode.com/problems/balance-a-binary-search-tree/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inorder(root):
            if(root is None):
                return []
            return inorder(root.left) + [root.val] + inorder(root.right)
        rst = inorder(root)
        def f(rst, l, r, tmp):
            if(l<=r):
                mid = int( (r -l)/2 + l )  
                tmp = TreeNode(rst[mid])
                tmp.left =    f(rst, l, mid -1, tmp.left)
                tmp.right =   f(rst, mid +1, r, tmp.right)   
            return tmp
        tmp = None            
        return f(rst, 0 , len(rst)-1, tmp)