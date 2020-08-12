'''https://leetcode.com/problems/range-sum-of-bst/'''
class Solution:
	def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
		rst = 0
		if not root : return rst
		stk = [root]
		while( stk):
			u = stk.pop()
			if L <= u.val <= R: rst+= u.val
			if u.left:
				stk.append(u.left)
			if u.right:
				stk.append(u.right)
		return rst
		