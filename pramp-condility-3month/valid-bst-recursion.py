'''
https://leetcode.com/problems/validate-binary-search-tree
'''
class Solution:
	def isValidBST(self, root):
		if root is None: return True
		lower , upper = float('-inf'), float('inf')
		stk = [(root, lower, upper ) ]
		while stk:
			
			u, lower, upper = stk.pop()
			if u.val <= lower or u.val >= upper :
				return False
			if u.right: stk.append((u.right,  u.val, upper))
			if u.left: stk.append((u.left, lower, u.val))
		return True