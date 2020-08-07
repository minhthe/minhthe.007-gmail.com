import heapq
class Solution:
	def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
		if root is None: return []
		mp = {}

		stk =[(root, 0 , 0 )]
		while stk:
			u, x, y  = stk.pop(0)
			if x not in mp:
				mp[x]= [(y*(-1), u.val)]
				heapq.heapify(mp[x]) 
			else:
				heapq.heappush(mp[x], (y*(-1), u.val))
			if u.left:
				stk.append( (u.left, x - 1, y - 1) )
			if u.right:
				stk.append( (u.right, x +1, y -1) )
		rst = []
		for key, value in sorted(mp.items(), key = lambda x: x[0]):
			s = []
			while len(value):
				tmp = heapq.heappop(value)
				s.append(tmp[1])
			rst.append(s)
		return rst