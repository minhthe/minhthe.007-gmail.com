'''https://leetcode.com/problems/binary-tree-inorder-traversal/'''
class Solution:
	def inorderTraversal(self, root: TreeNode) -> List[int]:
		stk = []
		rst = []
		while root or  stk:
			if root:
				stk.append(root)
				root  = root.left 
			else:
				cur = stk.pop()
				rst.append(cur.val)
				if cur.right:
					root = cur.right
		return rst