''''

https://leetcode.com/problems/house-robber-iii/

good explanation:
https://leetcode.com/problems/house-robber-iii/discuss/376297/Python3-Dynamic-Programming-%2B-Depth-First-Search

We construct a dp tree.
Each node (dp_node) in this dp tree is an array of two elements:
dp_node = [your gain when you ROB the current node, your gain when you SKIP the current node]

dp_node[0] =[your gain when you ROB the current node]
dp_node[1] =[your gain when you SKIP the current node]
we start by scanning from the leaf: Depth First Search

For each node you have 2 options:

option 1: ROB the node, then you can't rob the child/children of the node.
dp_node[0] = node.val + dp_node.left[1] + dp_node.right[1]
option 2: SKIP the node, then you can ROB or SKIP the child/children of the node.
dp_node[1] = max(dp_node.left[0], dp_node.left[1]) + max(dp_node.right[0], dp_node.right[1])
the maximum of gain of the node depents on max(dp_node[0],dp_node[1])

  """
    Input: [3,4,5,1,3,null,1]
 input tree            dp tree:
     3                  [3+3+1,4+5]
    / \                /        \
   4   5            [4,3]      [5,1]
  / \   \          /   \          \
 1   2   1      [1,0]  [2,0]     [1,0]
 
    
    
    """
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def rob(self, root: TreeNode) -> int:
		def f(root):
			if root is None: return (0,0)
			left =  f(root.left)
			right = f(root.right)
			return (root.val + left[1] + right[1], max(left[0], left[1]) + max(right[0], right[1]))
		return max(f(root))
    
        