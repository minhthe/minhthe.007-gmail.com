'''
https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
'''
class Solution:
	def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
		mp = {}
		if root is None: return []
		def f(root):
			que = [(root, 0)]
			while(len(que)):
				u, l = que.pop(0)
				if l in mp:
					mp[l].append(u.val)
				else:
					mp[l] = [u.val]
				if u.left:
					que.append( (  u.left, l + 1 ) )
					
				if u.right:
					que.append( (  u.right, l + 1 ) )		
		f(root)
		rst = []
		for i, v in sorted(mp.items(),  key = lambda x : x[0], reverse = True):
			rst.append(v)
		return rst
