'''
https://leetcode.com/problems/binary-tree-level-order-traversal-ii
'''
from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        mp = defaultdict(list)
        if root is None: return []
        def f():
            que = [(root, 0)]
            while(len(que)):
                u, v= que.pop(0)
                mp[v].append(u.val)
                if u.left: que.append((u.left, v+1))
                if u.right: que.append((u.right, v+1))
        rst = []
        f()
        for u,v in sorted(mp.items(), key= lambda x : x[0], reverse= True):
            rst.append(v)
        return rst
                    
        