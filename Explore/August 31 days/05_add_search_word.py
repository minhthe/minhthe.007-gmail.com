'''
https://leetcode.com/problems/add-and-search-word-data-structure-design/
'''
class Node:
	def __init__(self):
		self.child ={}
		self.cnt = 0
class WordDictionary:

	def __init__(self):
		self.root = Node()
		
	def addWord(self, word: str) -> None:
		tmp = self.root
		for c in word:
			if c not in tmp.child:
				tmp.child[c] = Node()
			tmp = tmp.child[c]
		tmp.cnt += 1 

	def search(self, word: str) -> bool:
		tmp = self.root
		
		pos = 0 
		
		def f(tmp,word, pos):
			if pos == len(word): 
				# print(pos, word[pos], tmp.cnt)
				if tmp.cnt > 0 : return True
				return False
			if word[pos]!='.':
				if word[pos] not in tmp.child:
					return False
				tmp = tmp.child[word[pos]]
				return f(tmp,word, pos+1)
			else:
				for item in tmp.child:
					if f(tmp.child[item], word,pos+1) : return True
			
				return False
				
		
		return f(tmp,word, pos)
			