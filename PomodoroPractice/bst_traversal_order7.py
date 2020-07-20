'''
https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
'''
import collections
class Solution:
	def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
		if root is None: return []
		mp = collections.defaultdict(list)
		rst = []
		def f(root, level):
			mp[level].append(root.val)
			if root.left:
				f(root.left, level + 1)
			if root.right: 
				f(root.right, level + 1)
			return mp
				
		for u,v in sorted(f(root, 0).items(), key= lambda x: x[0], reverse = True)				:
			rst.append(v)
		return rst