''''
https://leetcode.com/problems/n-ary-tree-level-order-traversal/
'''
class Solution:
	def levelOrder(self, root: 'Node') -> List[List[int]]:
		if root is None: return []
		rst = []
		traversal = [root]
		while( traversal):
			curr , next = [], []
			for node in traversal:
				curr.append(node.val)
				for child in node.children:
					next.append(child)
			rst.append(curr)
			traversal = next		
		return rst