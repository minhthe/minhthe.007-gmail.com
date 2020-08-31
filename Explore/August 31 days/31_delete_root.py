'''https://leetcode.com/problems/delete-node-in-a-bst/'''
class Solution:
	def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
		def minNode( root):
			while root.left:
				root = root.left
			return root
		if root is None: return 
		if key > root.val:
			root.right = self.deleteNode(root.right, key)
		elif key < root.val:
			root.left = self.deleteNode(root.left, key)
		
		else : 
			# if root.left is None and root.right is None: return None
			if root.right is None :
				tmp = root.left
				return tmp
			if root.left is None:
				tmp = root.right
				return tmp
			tmp = minNode(root.right)
			root.val = tmp.val
			root.right = self.deleteNode(root.right, tmp.val)
		return root
		