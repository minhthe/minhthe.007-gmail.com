'''https://leetcode.com/problems/path-sum-ii'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if root is None: return []
        rst = []
        
        def f(root, tmp, s):
            if root.left is None and root.right is None and s == sum:
                rst.append(tmp[:])
            if root.left:
                f(root.left, tmp + [root.left.val], s + root.left.val)
            if root.right:
                f(root.right, tmp + [root.right.val], s + root.right.val)
            return rst
        return f(root, [root.val], root.val)
        