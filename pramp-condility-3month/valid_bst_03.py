'''https://leetcode.com/problems/validate-binary-search-tree/'''

class Solution:
	def isValidBST(self, root: TreeNode) -> bool:
		if root is None: return True
		def f(root, lower, upper):
			if root is None: return True
			if not(lower < root.val < upper) : return False
			return f(root.left, lower, root.val) and f(root.right, root.val, upper)
	
		lower, upper = float('-inf'), float('inf')
		return f(root, lower, upper)