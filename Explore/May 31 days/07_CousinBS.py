'''
https://leetcode.com/problems/cousins-in-binary-tree/
'''
class Solution:
	def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
		mp = {}
		def f(root, x, y):
			queue  = [(root,0)]
			mp[root.val] = 0
			while(len(queue)):
				u, l = queue.pop(-1)
				if u.left and u.right and u.left.val == x and u.right.val == y:
					return False
				if u.left and u.right and u.left.val == y and u.right.val == x:
					return False										
				if u.left:
					queue.append((u.left, l+ 1))
					mp[u.left.val] = l + 1
				if u.right:
					queue.append((u.right, l + 1))
					mp[u.right.val] = l + 1
			return True
			
		ans = f(root, x, y)
		if(ans == True):
			if mp[x] == mp[y]: return True
			return False
		return False
  