'''https://leetcode.com/problems/balance-a-binary-search-tree'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def f(root):
            if not root: return []
            return f(root.left) + [root.val] + f(root.right)
        
        inorder = f(root)
        def f2(l, r):

            
            if r < l or l < 0 or r >= len(inorder) : return None
            
            if l == r: return TreeNode(inorder[l])
            
            mid = int( (r- l)/2 + l )
            
            tmp  = TreeNode(inorder[mid])
            
            tmp.left = f2(l, mid-1)
            
            tmp.right = f2(mid+1, r)

            return tmp
        
        return f2(0, len(inorder)-1)
