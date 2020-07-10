'''
https://leetcode.com/problems/binary-tree-level-order-traversal/
'''
from collections import deque
from collections import defaultdict
class Solution:
	def levelOrder(self, root: TreeNode) -> List[List[int]]:
		if root is None: return []
		mp = defaultdict(list)
		
		def f():
			stk = deque([(root, 0 )])
			while(len(stk)):
				u, v = stk.popleft()
				mp[v].append(u.val)
				if u.left: stk.append((u.left, v+1))
				if u.right: stk.append((u.right, v+1))
			return mp
				
		f()
		
		return mp.values()
	