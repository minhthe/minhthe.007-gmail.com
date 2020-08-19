'''
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
'''
class Solution:
	def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
	
		# if root is None or p is None or q is None: return None
		if root.val >= min(q.val, p.val) and root.val <= max(q.val, p.val) : return root
		if root.val > max(q.val, p.val): return self.lowestCommonAncestor(root.left, p, q )
		if root.val < min(q.val, p.val): return self.lowestCommonAncestor(root.right, p, q )