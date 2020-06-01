'''
https://leetcode.com/problems/invert-binary-tree/
'''
class Solution:
	def invertTree(self, root: TreeNode) -> TreeNode:
		if root is None: return None
		ll = root.left
		rr = root.right
		root.left = self.invertTree(rr)
		root.right = self.invertTree(ll)
		return root