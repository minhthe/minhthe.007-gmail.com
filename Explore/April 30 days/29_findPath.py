'''
https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/532/week-5/3315/discuss/604465/Python-BFS-Solution
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        
        
        def bfs(root, arr):
            
            if root is None or root.val != arr[0]:
                return False
            queue = [(root, 1)]
            while( len(queue)):
                
                u,v = queue.pop(0)
                
                if (u.left is None and u.right is None and v == len(arr)):
                    return True
                
                if( v == len(arr) and (u.left or u.right) ): return False
                
                if u.left and u.left.val == arr[v]:
                    queue.append((u.left, v + 1))
                    
                if u.right and u.right.val == arr[v]:
                    queue.append((u.right, v + 1))
                            
            return False
                
            
        rst = bfs(root, arr)
        return rst
        