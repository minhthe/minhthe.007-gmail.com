'''
https://leetcode.com/problems/implement-trie-prefix-tree
'''

class Node:
	def __init__(self):
		self.child = {}
		self.cnt = 0 
class Trie:

	def __init__(self):
		self.root = Node()
		
		

	def insert(self, word: str) -> None:
		tmp = self.root
		for c in word:
			if c not in tmp.child:
				tmp.child[c] = Node()
			tmp = tmp.child[c]
		tmp.cnt += 1 

	def search(self, word: str) -> bool:
		tmp = self.root
		for c in word:
			if c not in tmp.child:
				return False
			tmp = tmp.child[c]
		return tmp.cnt > 0
        

	def startsWith(self, prefix: str) -> bool:
		tmp = self.root
		for c in prefix:
			if c not in tmp.child:
				return False
			tmp = tmp.child[c]
		return True