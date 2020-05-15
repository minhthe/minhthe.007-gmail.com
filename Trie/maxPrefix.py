'''
https://leetcode.com/problems/longest-common-prefix
'''
class Node:
	def __init__(self):
		self.child = {}
		self.cntWord = 0
		self.content = ""
		self.w = ""
class Tree:
	def __init__(self):
		self.root = Node()

	def addNode(self, word):
		tmp = self.root
		rst =  ""
		for ch in word:
			if ch not in tmp.child:
				tmp.child[ch] = Node()
				tmp.content = rst + ch
				tmp.w = ch
			rst = tmp.content
			tmp = tmp.child[ch]

		tmp.cntWord +=1 
	
	def longPrefix(self, min_v):
		tmp = self.root
		rst = ""
		while(len(tmp.child) == 1 and len(rst) < min_v):
			rst = tmp.content
			tmp = tmp.child[tmp.w]
		return rst
		
class Solution:
	def longestCommonPrefix(self, strs: List[str]) -> str:
		tree = Tree()
		min_v = int(1e9)
		for item in strs:
			if len(item):
				tree.addNode(item)
				min_v = min(min_v, len(item))
			else:
				return ""
		return tree.longPrefix(min_v)