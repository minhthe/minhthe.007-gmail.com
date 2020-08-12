'''https://leetcode.com/problems/range-sum-of-bst/'''
class Solution:
	def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
		if not root :return 0
		l = self.rangeSumBST(root.left, L, R)
		r = self.rangeSumBST(root.right, L, R)
		return l + r + root.val if  L <= root.val <= R else l + r