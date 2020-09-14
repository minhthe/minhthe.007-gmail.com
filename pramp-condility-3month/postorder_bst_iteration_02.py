''''https://leetcode.com/problems/binary-tree-postorder-traversal'''
class Solution:
	def postorderTraversal(self, root: TreeNode) -> List[int]:
		rst , stk= [] , []
		while root or stk:
			if root:
				rst.append(root.val)
				stk.append(root)
				root = root.right
			else:
				u = stk.pop()
				if u.left:
					root = u.left
		return rst[::-1]