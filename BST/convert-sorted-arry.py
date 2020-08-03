'''
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def f(l,r):
            
            
            if l > r: return None
            
            mid = int( (r-l)/2 + l )
            node = TreeNode(nums[mid])
            node.left = f(l, mid - 1)
            node.right = f(mid+1, r)
            return node
        return f(0, len(nums)-1)