'''
https://leetcode.com/problems/binary-tree-inorder-traversal/
'''
class Solution:
	def inorderTraversal(self, root: TreeNode) -> List[int]:
		
		stk = []
		rst = []
		tmp = root
		while(tmp or len(stk)):
			while(tmp):
				stk.append(tmp)
				tmp = tmp.left
			u = stk.pop()
			rst.append(u.val)
			tmp = u.right
		return rst