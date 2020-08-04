'''
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal
'''
class Solution:
	def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
		mp={inorder[i]:i for i in range(len(inorder))}
		left, right = 0 , len(preorder) - 1
		idx = [0]
		def buildBS(left , right):
			if left > right: return None
			node = TreeNode(preorder[idx[0]])
			mid = mp[preorder[idx[0]]]
			idx[0] += 1
			
			if left == right: return node
			

			
			node.left = buildBS(left, mid - 1)
			node.right = buildBS(mid + 1, right)

			return node
			
		return buildBS(left , right)