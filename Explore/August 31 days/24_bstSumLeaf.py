'''https://leetcode.com/problems/sum-of-left-leaves/'''
class Solution:
	def sumOfLeftLeaves(self, root: TreeNode) -> int:
		
		rst = 0 
		if root is None: return rst
		stk = [(root, 0 )]
		
		while stk:
			u , l = stk.pop()
			if l & 1 and u.left is None and u.right is None: rst += u.val
			if u.left : stk.append(  (u.left, 2*l + 1) )
			if u.right : stk.append(  (u.right, 2*l + 2) )
			
		return rst