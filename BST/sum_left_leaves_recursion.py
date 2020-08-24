'''https://leetcode.com/problems/sum-of-left-leaves/'''
class Solution:
	def sumOfLeftLeaves(self, root: TreeNode) -> int:
		
		def f(root, flag):
		
			if root is None: return 0
			if flag and root.left is None and root.right is None: return root.val
			return f(root.left, True) + f(root.right, False)
		
		return f(root,False)