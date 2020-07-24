'''
https://leetcode.com/problems/n-ary-tree-preorder-traversal/
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None: return []
        tmp = [root.val]
        for item in root.children:
            tmp +=  self.preorder(item)
        
        return tmp