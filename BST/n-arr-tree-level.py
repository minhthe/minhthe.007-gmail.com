'''
https://leetcode.com/problems/n-ary-tree-level-order-traversal/
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
import collections
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None: return []      
        mp = collections.defaultdict(list)
        def f():
            que = collections.deque([(root, 0)])
            while(len(que)):
                u,v = que.popleft()
                mp[v].append(u.val)
                for child in u.children:
                    que.append( ( child, v+1 ) )         
        f()
        return mp.values()