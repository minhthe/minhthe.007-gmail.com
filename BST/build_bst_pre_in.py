
'''
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        mp = {inorder[i]: i for i in range(len(inorder))}
        
        cnt = [0]
        
        left , right = 0, len(inorder) - 1
        
        def build(left, right):
            
            if left > right: return None            
            
            
            node = TreeNode(preorder[cnt[0]])
            k =  mp[preorder[cnt[0]]] 
            cnt[0] += 1
            if left == right: return node
            
            node.left = build( left, k - 1)
         
            node.right = build( k + 1, right)
         
            return node
            
        
        return build( left, right)
        