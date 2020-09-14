'''https://leetcode.com/problems/binary-tree-inorder-traversal/'''
class Solution:
	def inorderTraversal(self, root: TreeNode) -> List[int]:
		rst, stk = [], [] 
		while root or stk:
			if root:
				stk.append(root)
				root = root.left
			else:
				u = stk.pop()
				rst.append(u.val)
				if u.right:
					root = u.right
		return rst