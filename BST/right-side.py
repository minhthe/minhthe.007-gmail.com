'''
https://leetcode.com/problems/binary-tree-right-side-view
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        rst =  []
        if root is None: return []
        if root: rst = [root.val]
        travel = [root] 
        while travel:
            current = []
            
            for item in travel:
                if item.left:
                    current.append(item.left)
                if item.right:
                    current.append(item.right)
            if current : rst.append(current[-1].val)
            travel = current 
        return rst