'''https://leetcode.com/problems/binary-tree-postorder-traversal'''
class Solution:
	def postorderTraversal(self, root: TreeNode) -> List[int]:
		if root is None: return []
		rst = []
		
		stk = [root]
		while stk:
			u  = stk.pop()
			rst.append(u.val)
			if u.left: stk.append(u.left)
			if u.right: stk.append(u.right)
			
		
		return rst[::-1]
		