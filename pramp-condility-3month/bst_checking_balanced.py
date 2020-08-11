'''https://leetcode.com/problems/balanced-binary-tree/'''
class Solution:
	def isBalanced(self, root: TreeNode) -> bool:
		if root is None: return True
		
		def getHeight(root):
			if root is None: return 0
			return max( getHeight(root.left),  getHeight(root.right) ) + 1
	
		return self.isBalanced(root.left) and self.isBalanced(root.right) and abs( getHeight(root.left) - getHeight(root.right)) <= 1