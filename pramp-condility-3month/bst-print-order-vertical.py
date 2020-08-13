'''https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree'''
class Solution:
	def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
		if not root: return []
		mp = {}
		rst = []
		stk = [(root,0, 0 )]
		while(stk):
			u , v , y  = stk.pop()
			if v not in mp:
				mp[v] = [(-y,u.val)]
				heapq.heapify(mp[v])
			else:
				heapq.heappush( mp[v], (-y, u.val))
			
			if u.left:
				stk.append(  (u.left, v - 1, y -1) )
			if u.right:
				stk.append(  (u.right, v + 1,  y - 1 ) )
		
	
		for u,v in sorted(mp.items(), key = lambda x : x[0]):
			tmp = []
			while v:
				vv = heapq.heappop(v)
				tmp.append(vv[1])
			rst.append(tmp)	
		return rst