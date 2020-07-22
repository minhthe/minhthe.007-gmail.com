'''
https://leetcode.com/problems/n-ary-tree-preorder-traversal
'''
class Solution:
	def preorder(self, root: 'Node') -> List[int]:
		if root is None: return []
		rst = []
		def f(root):
			rst.append(root.val)
			for child in root.children:
				f(child)
			return rst	
		return f(root)