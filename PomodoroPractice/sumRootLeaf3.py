'''
https://leetcode.com/problems/sum-root-to-leaf-numbers

***noting:
this method is dfs not bfs
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        rst = []
        if root is None: return 0
        def bfs(rst):
            
            stk = [(root, str(root.val))]
            while(len(stk)):
                u,v = stk.pop()
                if u.left is None and u.right is None: 
                    rst.append(v)
                if u.left: 
                    stk.append( (u.left, v + str(u.left.val) ) )
                if u.right: 
                    stk.append( (u.right, v + str(u.right.val) )  )    
            return rst
        
        bfs(rst)
        
        return sum([int(item) for item in rst])