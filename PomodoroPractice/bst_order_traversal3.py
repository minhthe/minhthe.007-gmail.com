'''
https://leetcode.com/problems/binary-tree-level-order-traversal/
'''
import collections
class Solution:
	def levelOrder(self, root: TreeNode) -> List[List[int]]:
		if root is None: return []

		mp  = collections.defaultdict(list)
		def f(root):
			deque = [(root,0)]
			deque = collections.deque(deque)
			
			while(len(deque)):
				u, v = deque.popleft()
				mp[v].append(u.val)
				if u.left : deque.append((u.left, v+1))
				if u.right: deque.append((u.right, v+1))
			return mp
		
		return f(root).values()
		