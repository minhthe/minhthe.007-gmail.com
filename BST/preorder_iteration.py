'''https://leetcode.com/problems/binary-tree-preorder-traversal/s'''
class Solution:
	def preorderTraversal(self, root: TreeNode) -> List[int]:
		rst= []
		stk = []
		while root or stk:
			if root:
				rst.append(root.val)
				stk.append(root)
				root = root.left
			else:
				u = stk.pop()
				if u.right:
					root = u.right
						
		return rst