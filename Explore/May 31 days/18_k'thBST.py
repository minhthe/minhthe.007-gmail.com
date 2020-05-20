'''
https://leetcode.com/problems/kth-smallest-element-in-a-bst/
'''
class Solution:
	def kthSmallest(self, root: TreeNode, k: int) -> int:
		rst = []
		
		
		def f(root):
			if root:
				return f(root.left) + [root.val] + f(root.right)
			else:
				return []
		rst = f(root)
		return (rst)[k-1]