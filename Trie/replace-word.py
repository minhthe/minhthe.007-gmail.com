'''
https://leetcode.com/problems/replace-words/
'''

class Tree:
	def __init__(self):
		# print('here')
		self.root = Node()
	def addNode(self, s):
		tmp = self.root
		for c in s:
			# print(c, tmp.cnt)
			if c not in tmp.child:
				tmp.child[c] = Node()
			tmp = tmp.child[c]
		tmp.cnt +=1 
	
	def startswith(self, s) :
		tmp = self.root
		rst = ""
		for c in s:
			if c not in tmp.child:
				if tmp.cnt >= 1: 
					return rst
				else:
					return s 
			rst += c
			if len(tmp.child):
				tmp = tmp.child[c]                
				if tmp.cnt >= 1:
					return rst			
				# tmp = tmp.child[c]
			else:
				if tmp.cnt >= 1:
					return rst			
		return s
class Node:
	def __init__(self):
		# print('node hjere')
		self.cnt =  0 
		self.child = {}
class Solution:
	def replaceWords(self, dict: List[str], sentence: str) -> str:
		
		rst = []
		tmp = sentence.split(" ")
		tree = Tree()
		node = Node()
		for item in dict:
			tree.addNode(item)
			
				
		for item in tmp:
			rst.append(tree.startswith(item) )
		return ' '.join(rst)