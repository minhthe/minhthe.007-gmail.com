'''https://leetcode.com/problems/validate-binary-search-tree'''
class Solution:
	def isValidBST(self, root: TreeNode) -> bool:
		
		pre = float('-inf')
		stk = []
		while stk or root:
			if root:
				stk.append(root)
				root = root.left
			else:
				cur = stk.pop()
				if cur.val <= pre: return False
				pre = cur.val
				if cur.right:
					root = cur.right
		return True