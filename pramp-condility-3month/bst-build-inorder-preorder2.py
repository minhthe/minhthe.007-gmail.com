'''
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/'''
class Solution:
	def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
		if inorder:
			p = preorder.pop(0)
			# print(p, inorder)
			mid = inorder.index(p)
			node = TreeNode(p)
			node.left = self.buildTree(preorder, inorder[:mid])
			node.right = self.buildTree(preorder, inorder[mid+1:])
			return node