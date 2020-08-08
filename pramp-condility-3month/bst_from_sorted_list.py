'''
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        l, r = 0, len(nums)-1
        if len(nums) == 0: return None
        def f(l,r):
            if l> r: return None
             #   0  1  2 3 4
            # [-10,-3,0,5,9],
            mid = (l+r)//2
            root = TreeNode(nums[mid])
            root.left = f(l,mid-1) # 0, 1
            root.right = f(mid + 1, r)
            return root
            
            
            
            
        return f(l,r)