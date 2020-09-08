'''https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/s'''
class Solution:
	def sumRootToLeaf(self, root: TreeNode) -> int:
		rst = []
		if root is None: return 0
		
		def f(root, tmp):
			if root.left  is None and root.right is None: 
				rst.append(tmp[:])
			if root.left:
				f(root.left, tmp + [root.left.val])
			if root.right:
				f(root.right, tmp + [root.right.val])
			return rst
		rst = f(root,[root.val])			
		s =  0 
		def f2(nums):
			t = 0 
			nums = nums[::-1]
			for i,v in enumerate(nums):
				if v == 1: t += 2**(i)
			return t
		for item in rst:
			s += f2(item)
		return s
