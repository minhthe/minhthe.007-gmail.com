''''

https://leetcode.com/problems/binary-tree-level-order-traversal
''''

class Solution:
	def levelOrder(self, root: TreeNode) -> List[List[int]]:
		if root is None:return  []
		rst = []
		
		travel = [root]
		while(len(travel)):
			curr , next = [] , []
			for node in travel:
				curr.append(node.val)
				if node.left:
					next.append(node.left)
				if node.right:
					next.append(node.right)
			rst.append(curr)
			travel = next
		return rst