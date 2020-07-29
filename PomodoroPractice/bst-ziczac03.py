'''
https://leetcode.com/problems/binary-tree-level-order-traversal/
'''
class Solution:
	def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
		if root is None: return []
		rst = []
		
		travel = [root]
		reverse = False
		while travel: 
			curr, next= [],[]
			for node in travel:
				curr.append(node.val)
				if node.left: next.append(node.left)
				if node.right: next.append(node.right)
			rst = rst + [curr[::-1]] if reverse else rst + [curr]
			reverse = not reverse
			travel = next
			
		return rst