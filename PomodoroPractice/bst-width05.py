'''
https://leetcode.com/problems/maximum-width-of-binary-tree/
'''
import collections
class Solution:
	def widthOfBinaryTree(self, root: TreeNode) -> int:
		if root is None: return 0
		rst = 1
		mp = collections.defaultdict(list)
		
		
		def f(root):
			
			stk = [(root, 0, 0 )]
			while len(stk):
				u, v , p = stk.pop()
				mp[v].append(p)
				if u.left:
					stk.append( ( u.left, v + 1, 2* p + 1 ) )
				if u.right:
					stk.append( ( u.right, v + 1, 2* p + 2 ) )
					
			return mp
					
			
			
		mp = f(root)
		list_v = mp.values()
		
		for item in list_v:
			if len(item) > 1:
				rst = max(rst, max(item) - min(item)  + 1)
		
		return rst