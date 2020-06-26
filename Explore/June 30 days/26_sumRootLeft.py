'''
https://leetcode.com/problems/sum-root-to-leaf-numbers/
'''
class Solution:
	def sumNumbers(self, root: TreeNode) -> int:
		if root is None: return 0
		rst = []
		
		def f1(root):
			
			
			stk =[ (root, str(root.val) ) ]
			while(len(stk)):
				u, v = stk.pop()
				if u.left is None and u.right is None: rst.append(v)
				if u.left:
					stk.append( (u.left,  v + str(u.left.val)) )
				if u.right:
					stk.append( (u.right, v + str(u.right.val))  )
				
				
				
		f1(root)
		
		print(rst)
		def f2(rst):
			s = 0 
			for item in rst:
				s+= int(item)
			return s
		return f2(rst)