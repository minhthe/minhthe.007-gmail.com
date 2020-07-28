'''
https://leetcode.com/problems/same-tree
'''
class Solution:
	def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
		
		if p is None and q is None: return True
		
		stk = [(p,q)]
		while(len(stk)):
			u,v = stk.pop()
			if u is None and v is None: continue
			if u is None or v is None: return False	
			if u.val != v.val: return False
			if u and v :				
				stk.append((u.left, v.left))
				stk.append((u.right, v.right))
			
		
		
		return True