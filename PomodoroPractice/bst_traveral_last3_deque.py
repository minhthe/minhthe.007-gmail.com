''''
https://leetcode.com/problems/binary-tree-level-order-traversal-ii
''''
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        de = deque([])
        if root is None: return []
        de.append( (root, 0) )
        rst = []
        while(len(de)):
            
            u, v = de.popleft()
            if len(rst) < v + 1: 
                rst.append([])
            rst[v].append(u.val)
            if u.left: de.append( (u.left, v + 1) )
            if u.right: de.append( (u.right, v + 1) )
                
            
        return rst[::-1]  