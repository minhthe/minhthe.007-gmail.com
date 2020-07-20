'''
https://leetcode.com/problems/binary-tree-level-order-traversal/
'''
import collections
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None: return []
        rst = []
        
        first = collections.deque([root])
        tmp = []
        while(len(first)):
            l = len(first)
            tmp = []
            for _ in range(l):
                u = first.popleft()
                tmp.append(u.val)
                
                if u.left: first.append(u.left)
                if u.right: first.append(u.right)
            rst.append(tmp)           
        return rst