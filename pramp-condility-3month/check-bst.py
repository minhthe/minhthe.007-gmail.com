class Solution:
	def isValidBST(self, root: TreeNode) -> bool:
		if root is None : return True
		
		def f(root):
			if root is None: return []
			return f(root.left) + [root.val] + f(root.right)
		rst =  f(root) 
		return rst == sorted(list(set(rst)))