'''
https://leetcode.com/problems/n-ary-tree-level-order-traversal
'''
import collections
class Solution:
	def levelOrder(self, root: 'Node') -> List[List[int]]:
		mp= collections.defaultdict(list)
		if root is None: return []
		def f(root, level):
			if root is None: return 
			mp[level].append(root.val)
			for child in root.children:
				f(child, level+1)
			return mp
		
		return f(root, 0).values()