'''https://leetcode.com/problems/delete-node-in-a-bst/'''
class Solution:
	def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
		if root is None: return root
		if root.val > key:
			root.left = self.deleteNode(root.left, key)
		elif root.val < key:
			root.right = self.deleteNode(root.right, key)
		else:
			if root.left is None:
				return root.right
			if root.right is None:
				return root.left 
			else:
				tmp = root.right
				while tmp.left:
					tmp = tmp.left
				root.val = tmp.val
				root.right = self.deleteNode(root.right, tmp.val)
		return root