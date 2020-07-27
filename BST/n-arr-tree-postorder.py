'''
https://leetcode.com/problems/n-ary-tree-postorder-traversal/
'''
class Solution:
	def postorder(self, root: 'Node') -> List[int]:
		if root is None: return []
		if (root.children) is None: 
			return [root.val]
		rst = []
		for child in root.children:
			rst = rst + self.postorder(child) 
		return rst + [root.val]
