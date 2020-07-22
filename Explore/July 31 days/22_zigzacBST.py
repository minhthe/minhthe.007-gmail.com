'''
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
'''
import collections
class Solution:
	def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
		if root is None: return []
		mp = collections.defaultdict(list)
		
		def f(root):
			
			deque = collections.deque([(root, 1)])
			while(len(deque)):
				
				u, v = deque.popleft()
				mp[v].append(u.val)
				if u.left :
					deque.append( (u.left, v + 1) )
				if u.right :
					deque.append( (u.right, v + 1) )
				
			return mp
		rst = []								
		mp = f(root)
		
		for key in mp:
			if key & 1 : 
				rst.append(mp[key])
			else:
				rst.append(mp[key][::-1])
		return rst
		