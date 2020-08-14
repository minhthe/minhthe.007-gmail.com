'''
https://leetcode.com/problems/invert-binary-tree/
Space complexity is O(n)O(n), since in the worst case, the queue will contain all nodes in one level of the binary tree. For a full binary tree, the leaf level has [n/2]=O(n) leaves.

'''
class Solution:
	def invertTree(self, root: TreeNode) -> TreeNode:
	
		if not root: return root
		que = [root]
		while que:
			u = que.pop(0)
			tmp = u.left
			u.left = u.right
			u.right = tmp
			if u.left:
				que.append(u.left)
			if u.right:
				que.append(u.right)
		return root