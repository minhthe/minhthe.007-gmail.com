'''
https://leetcode.com/problems/maximum-width-of-binary-tree/
'''
from collections import defaultdict
class Solution:
	def widthOfBinaryTree(self, root: TreeNode) -> int:
		if root is None: return 0
		mp = defaultdict(lambda : [ int(1e9),-int(1e9)]  )
		def f(root):
			stk = [(root, 0, 0 )]

			while(len(stk)):
				
				u, v , l = stk.pop()
				if u.left:
					stk.append( (u.left, v*2+1, l + 1) )
					mp[l][0] = min( mp[l][0], v*2+1 )
					mp[l][1] = max( mp[l][1], v*2+1 )
				if u.right:
					stk.append( (u.right, v*2+2, l + 1) )
					mp[l][1] = max( mp[l][1], v*2+2 )
					mp[l][0] = min( mp[l][0], v*2+2 )
			rst = 1
			# print(mp)
			for u,v in mp.values():
				if u==int(1e9) or v== -int(1e9): continue
				rst = max(rst, v- u + 1)
			return rst
		return f(root)