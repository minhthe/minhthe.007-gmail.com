'''https://leetcode.com/problems/path-sum-ii/'''# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if root is None: return []
        rst = []
        
        stk = [(root, [root.val] , root.val)]
        while stk:
            u, tmp , s = stk.pop()
            # print(u.val,tmp,s)
            if u.left is None and u.right is None and s == sum:
                rst.append( tmp )
            if u.left:
                tmp2 = tmp[:]
                tmp2.append(u.left.val)
                stk.append( (u.left, tmp2, s + u.left.val) )
            if u.right:
                tmp2 = tmp[:]
                tmp2.append(u.right.val)
                stk.append( (u.right, tmp2, s + u.right.val) )
        return rst