'''https://leetcode.com/problems/binary-tree-preorder-traversal/'''
class Solution:
	def preorderTraversal(self, root: TreeNode) -> List[int]:
		rst = [] 
		stk = []
		while True:
			if root :
				rst.append(root.val)
				stk.append(root)
				root = root.left
			elif stk:
				u = stk.pop()
				if u.right:
					root = u.right
			else:
				return rst
		return rst