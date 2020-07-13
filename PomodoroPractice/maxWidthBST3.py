'''
https://leetcode.com/problems/maximum-width-of-binary-tre
'''
import collections
class Solution:
	def widthOfBinaryTree(self, root: TreeNode) -> int:
		if root is None: return 0
		mp= collections.defaultdict(list)
		def f():
			stk = [(root, 0, 0 )]
			
			while(len(stk)):
				u,v,l = stk.pop()
				if u.left:
					stk.append(  ( u.left,  v*2+1 , l+1) )
					mp[l+1].append(v*2+1)
				if u.right:
					stk.append( (u.right, v*2+2, l +1 ))
					mp[l+1].append(v*2+2)
			ans = 1
			for item in mp.values():
				if len(item) >=2:
					ans = max(ans, max(item) - min(item) + 1)
			return ans
				
				
		
		
		return f()