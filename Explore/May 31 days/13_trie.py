'''
https://leetcode.com/problems/implement-trie-prefix-tree/
'''

class Node:
	def __init__(self):
		self.child = {}
		self.cntWord = 0

class Trie:

	def __init__(self):
		self.root = Node()
		

	def insert(self, word: str) -> None:
		tmp = self.root
		for ch in word:
			if ch not in tmp.child:
				tmp.child[ch] = Node()
			tmp = tmp.child[ch]
		tmp.cntWord +=1
		

	def search(self, word: str) -> bool:

		tmp = self.root
		for ch in word:
			if ch not in tmp.child:
				return False
			tmp = tmp.child[ch]
		return tmp.cntWord > 0

	def startsWith(self, prefix: str) -> bool:

		tmp = self.root        
		for ch in prefix:
			if ch not in tmp.child:
				return False
			tmp = tmp.child[ch]
		return True